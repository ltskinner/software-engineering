# Chapter 3. Storage and Retrieval

On the most fundamental level, a database needs to do two things:

- when you give it some data, it should store it
- when you ask for that data later, it should give it back to you

Big differences between storage engines that are optimized for transactional workloads, and those optimized for analytics

## Data Structures that Power your Database

Many dbs internally use a log - which is an append-only data file

an `index` is an additional structure that is derived from the primary data

Maintaining structures does increase overhead, especially on write

- well chosen indexes speed up read queries
- every index will slow down writes

### Hash Indexes

Some important issues

- File format
  - CSV is not the best format for a log.
  - its faster and simpler to use a binary format that first encodes the length of a string in bytes, followed by the raw string (no need for escaping)
- Deleting records
  - if you want to delete a key and its associated value, you have to append a special deletion record to the data file (sometimes called a `tombstone`)
  - when the log sebments are merged, the tombstone tells the merging process to discard any previous value for the deleted key
- Crash recovery
  - if the database is restarted, the in-memory hash maps are lost
  - in principle, you can restore each segments hash map by reading the entire segment file from the beginning to end
- Partially written records
  - db may crash at any time, including half way through appending a record to the log
- Concurrency control
  - as writes are appended to the log in a strictly sequential order, a common implementation choice is to only have one writer thread
  - data file segments are append only and otherwise immutable, so they can be read concurrently by multiple threads

Append only design is good for several reasons:

- Appending and segment merging are sequential write operations, which are generally much faster than random writes
- Concurrency and crash recovery are much simpler if segment files are append-only or immutable - dont have to worry about splices
- Merging old segments avoids the problem of data files getting fragmented over time

However, hash table index also has limitations:

- hash table must fit in memory, so if you have a lot of keys, out of luck. You can put it on disk, but requires lots of random access io
- range queries are not efficient - have to look up each key individually in the hash map

### SSTables and LSM-Trees

Change: require that the sequence of key-value pairs is `sorted by key` - Sorted String Table

Several big advantages over log segments with hash indexes:

- Merging segments is simple and efficient, even if the files are bigger than the available memory
- In order to find a particular key in the file, you no longer need to keep an index of all the keys in memory
- Since read requests need to scan over several key-value pairs in the requested range anyway, it is possible to group those records into a block and compress it before writing to disk

#### Constructing and maintaining SSTables

how do you get your data to be sorted by key in the first place - use tree structures like red-black or avl

- when a write comes in, add it to an in-memory balanced tree structure - called a memtable
-  when the memtable gets bigger than some threshold (typically a few mb) write it out to disk as an sstable. new sstable file becomes the most recent segment of the database
- in order to serve a read request, first try to find the keys in the memtable, then on the most recent on-disk segement, then the next-older, etc
- from time to time, run a merging and compaction process in the background to combine segment files and to discard overwritten or deleted values

Works well, only one problem: if the db crashes, the most recent writes (which are in the memtable but not yet to disk) are lost

To address, create a separate log on disk in which every write is immediately appended, like the basic socultion above. every time a memtable is written out, the corresponding log can be discarded

#### Making an LSM-tree out of SSTables

Lucene, an indexing engine for full-text search used by elasticsearch and solr, uses a similar method for storing its term dictionary

#### Performance Optimizations

LSM-tree can be slow if the keys you are looking up do not exist in the database. Bloom filters, which approximate the contents of a set, can be used to address this

try size-tiered and leveled compaction

### B-Trees

Most widely used indexing structure

Keeps key-values pairs sorted by key, but have a very different design philosophy

B-trees break the db down into fixed-size blocks/pages, and read or write one page at a time. corresponds more closely to the underlying hardware

each page can be identified using an address or a location

one page is designated as the root of the b-tree

number of references to child pages in one page of the b-tree is called the branching factor - typically several hundred

four level b-trees with 4kb pages and a branching factor of 500 can store up to 250TB

#### Making B-trees Reliable

The basic underlying write operation of a B-tree is to overwrite a page on disk with new data. It is assumed that the overwrite does not change the location of the page (i.e all references to that page remain intact when the page is overwritten)

Many implementations include a write ahead log (WAT) aka redo log, which is an append-only file to which every b-tree modification must be written to before it can be applied to the pages of the tree itself

#### B-tree Optimizations

Many because have been around so long

- instead of overwriting pages and maintaining a wal for crash recovery, some dbs use a copy-on-write scheme
- save space in pages by not storing the entire key, just abbreviating it. packing more keys allows a tree to have a higher branching factor, and thus fewer levels
- lay out leaf pages to appear in sequential order on disk
- additional pointers are added to the tree, like references to left and right sibling, which allows scanning keys in order without jumping back to the parent
- b-tree variants such as fractal trees borrow some log-structured ideas to reduce disk seeks

### Comparing B-Trees and LSM-Trees

General rule of thumb:

- lsm-trees faster for writes
- b-trees faster for reads

But, need to check for your specific use case

#### Advantages of LSM-trees

- b-tree index must write every piece of data twice (one to write ahead log, and one to tree page itself)
  - write amplification - one write to the db resulting in multiple writes to disk
  - BAD for ssds
- lsm-trees are typically able to sustain higher write throughput than b-trees, partially because they have lower write amplificaiton, and partially because they sequentially write compact sstable files rather than having to overwrite several pages in the tree
- lsm-trees can be compressed etter

#### Downsides of LSM-trees

- compaction process can sometimes infterfere with the performance of ongoing reads and writes
- high-throughput issues with compaction: the disks finite write bandwidth needs to be shared between the initial write and compaction threads

### Other Indexing Structures

thus far, key-value indexes are like a `primary key` index in the relational model

also common to have `secondary indexes`

#### Storing Values Within the Index

while the key is something that queries search for, the value can be one of two things: the actual row (document or vertex), or it could be a reference to the row stored elsewhere. the latter case, the place where the rows are stored is known as a `heap file`, and stores data in no particular order

the heap file is common because it aboids diplicating data when multiple secondary indexes are present: each index just references a location in the heap file, and the actual data is kept in one place

in some cases, the extra hop from the index to the heap is too big of a penalty onreads, so it can be desirable to store the indexed row directly within an index - known as `clustered index`

MySQL InnoDB engine, the primary key of a table is always a clustered index, and the secondary indexes refer to the primary key (rather than a heap file location)

A compromise between a clustered index (storing all row data within the index) and a nonclustered index (storing only references to the data within the index) is known as a `covering index` or `index with included columns`, which store some of the table scolumns within the index. this allows some queries to be answered by using the index alone (in which case, the index is said to `cover` the query)

#### Multi-Column Indexes

Most common type is called a `concatenated index`, which simply combines several fields into one key by appending one column to another

These are a more general way of querying several columns at once, which is particularly important for geospatial data

#### Full-Text Search and Fuzzy Indexes

woo fuzzy bro no way, goddam i bet thats expensive tho

Levenshtein automaton no shit

#### Keeping Everything in Memory

redis and couchbase provide weak durability by writing to disk asynchronously

## Transaction Processing or Analytics

access patterns known as `online transaction processing` OLTP

for analytics, queries need to scan over a huge number of records, only reading a few columns per record, and calcuales aggregate statistics

becomes `online analytic processing` OLAP

| property | OLTP | OLAP |
| - | - | - |
| Main read pattern | small number of records per query, fetched by key | aggregate over large number of records |
| Main write pattern | Random-access, low-latency writes from user input | bulk import (ETL) or event stream |
| Primarily used by | end user/customer, via web application | Internal analyst, for decision support |
| What data represents | latest state of data (current point in time) | History of events that happened over time |
| Dataset size | gigabytes to terabytes | terabytes to petabytes |

### Data Warehousing

Db administrators of oltp dbs are super protective of production resources, and dont let stupid analysts run queries (for good reason lmao)

data warehouses, by contrast, is a separate database that analysts can query to their heards content, without affecting oltp operations

data warehouses can also be optimized for analytic access patterns - indexes that work well for oltp dont work great for olap, and vice versa

#### The Divergence Between OLTP DBs and Data Warehouses

### Stars and Snowflakes: Schemas for Analytics

star schema aka dimensional modeling

dimensions represent the who, what, where, when, how, and why of an event

variation of star is snowflake

- here, dimensions are further broken down into subdimensinos
  - e.g. separate tables for brands and product categories
  - edge tables in turn reference further edge tables

## Column-Oriented Storage

dont store all the values from one row together, but store all the values from each column together

if each column is stored in a separate file, a query only needs to read and parse those columns that are used inthe query, which can save a lot of work

if you need to reconstruct a row, take the index XXX from every column and slam together

### Column Compression

column-oriented lends itself very well to compression, especially if set of possible values and those just get reused (like country or state or whatever)

### Memory Bandwidth and Vectorized Processing

big bottleneck os getting data from disk into memory

cpu memory also becomes an issue

a query engine can take a chunk of compressed column data that fits into the cpus l1 cache, and iterate thu it in a tight loop (no function calls) - looping is faster than function calls - this is `vectorized processing`

### Sort Order in Column Storage

### Writing to Column-Oriented Storage

Optimizations make sense in data warehouses, because most of the load consists of large read-only queries run by analysts.

Column oriented storage, compression, and sorting make reads fast

writes become much more difficult

### Aggregation: Data Cubes and Materialized Views

so for like the same query over and over use data cubes and views

but these wont be good if you are exploring because they are just fiews

most data warehouses try to keep as much raw data as possible, and use aggregates such as data cubes only as a performance boost for certain queries
