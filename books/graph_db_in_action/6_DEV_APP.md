# Chapter 6. Developing an Application

## 6.1 Starting the project

## 6.2 Connecting to out database

## 6.3 Retrieving data

### 6.3.1 Retrieving a vertex

### 6.3.3 Adding terminal steps

Note: forgetting to force the evaluation of a traversal is one of the most common problems we encounter when debugging applications. This oversight bites even the most experienced of us from time to time

terminal steps:

- `.hasNext()` - returns a boolean value: true if there are available results, false if there are no results
- `.tryNext()` - a convienence method that is a combination of the hasNext() and next() steps to execute the traversal if there are available results. It returns a java Optional and is only available in JVM languages like java and groovy
- `.toList()` returns the list of the traversal as a List
- `.toSet` returns the results of the traversal as a Set

### 6.3.4 Creating the Java method in our application

## 6.4 Adding, modifying, and deleting data

### 6.4.1 Adding vertices

## 6.5 Translating our list and path traversals
