# Identifying Areas Likely to Change

* A great study of designers found that one attribute they all ahd in common was the ability to anticipate change
* Goal is to **isolate unstable areas** so that the effects of a change will be limited to one routine, class, or package

## Steps

### 1. Identify items that seem likely to change

* If reqs done well, they include a list of potential changes and the likelihood of each change

### 2. Separate items that seem likely to change

* Compartmentalize each volatile component into **separate classes**

### 3. Isolate items that seem likely to change

* Design interfaces to be insensitive to potential changes
* Any other class using the changed class should be unaware that the change occured

## Anticipating Different Degrees of Change

* Design systems so that the effect/scope of the change is proportional to the change that will occur
* Start at core functionality (that wont change), then incrementally identify potential changes
  * Functionally
  * Qualitatively (threading, localizable)

## Typical Areas

* Business rules
  * tax laws, union renegotiates a contract, etc
* Hardware dependencies
  * screens, printers, keyboards, gpus, cpus
* **Input and Output**
  * application that creates its own data format will probably change
  * user level inputs and output formats will also change
  * positioning of fields on page, number of fields, sequence, etc
* Nonstandard language features
  * using extensions is a double edge sword b/c not be avail in all environments
* Difficult design and construction areas
  * first pass might be done poorly so want to have flexibility to make changes
  * compartmentalize and make change impacts minimal
* **Status variables**
  * Don’t use booleans, use enumerated type so can add options
  * **use access routines** rather than checking variable directly
* Data size constraints
  * use named constants

