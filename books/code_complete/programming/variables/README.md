# Variables

## Make Variable Declarations Easy

* Dont use implicit declarations
* Use naming conventions
* Cross reference variable names

## Variable Scope

* Keep declarations and their references close together
  * Short number of lines between uses
* Keep variables "live" for as short a time as possible
  * Good for minimizing complexity
  * Makes splitting into rouintes easy

## Naming Variables

* Name shouldn't be cute or sounds good
  * The variable and its name should be the same thing
* Name fully and accurately describes the entity the variable represents
* Speak to the problem, not the solution
  * Express the WHAT, not thw how
* Proper length is about 2-3 words without connectors
* Computed value operations go at end of name
  * Total, sum, max, min, record, string
  * `revenueTotal()` `expenseAverage`
  * Instead of `num` use `count, total, index`
* Use common opposites
  * Begin/end
  * Up/down
  * [Full list](./NAMES.md#Common-Opposites)

## [Naming Conventions](./NAMES.md)

### Why naming conventions

* Help you learn code more quickly on a project
  * Dont have to keep track of:
    * What Johns code looks like
    * What Claires code looks like
    * Anyone else on project
* Without conventions, can easily call the same thing two different names
  * `pointsTotal` vs `totalPoints`
  * This is mega confusing
* Emphasize relationships among related items

#### Any convention is better than no convention - no matter how arbitrary it is

## [Naming Specific Data Types](./DATA_TYPES.md)

## Names to Avoid

* Avoid misleading names or abbreviations
* Avoid names with similar meanings
  * If you can switch the names of two variables without hurting the program, then both need to be renamed
* Avoid variables with different meanings but similar names
  * `clientRecs` vs `clientReps`
  * Look similar but very different values
* Avoid names that sound familliar
  * `rap` and `wrap`
* Avoid numbers in names
  * `file1, file2, etc`
  * If the numbers really are important, use an array instead of spearate values
* Avoid words that are commonly misspelled in english
* Dont differentiate variable name solely by capitalization
