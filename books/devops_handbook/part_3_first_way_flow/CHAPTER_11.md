# Chapter 11: Enable and Practice Continouous Integration

The longer developers work on branches, the harder they become to merge

* When code merges are painful, we tend to do less of them, making future merges even worse
* CI was designed to solve this problem by making merges to the trunk a routine

## Increase HPs Lazer Jet Productivity by 10x

* CI and trunk based development
* Significant investments in test automation
* Creation of harware simulators so tests could be run virtually
* Reproduction of test failures on dev workstations
* New architectures to support running all printers off of a common build and release

"Without automated testing, CI is the fastest way to get a big pile of junk that never compiles or runs correctly"

* Reduced builds to on eper day, eventually doing 10-15 per day
* Went from 20 commits per day performed by a "build boss" to over 100 per day by individual developers
* Enabled developers to change or add **75k-100k** liner of code each day
* Reduced regression test times from 6 weeks to one day

### Other Stats

* Time spent on innovation and writing new features increased from 5% to 40%
* Overall dev costs were reduced by 40%
* Programs under development increased 140%
* Dev costs cut by 78%

## Small Batch Dev

* Extreme 1:
  * Optimized for Individual Productivity
  * Everyone works on their own branch
  * Merging gets difficult
* Extreme 2:
  * Optimized for Team Productivity
  * Everone works on trunk
  * Each commit can break the build

### Side Effects

* When merging is difficult, we become less able and less motivated to improve and refactor code
  * this is because refactors are more likely to cause rework for everyone else

"When we do not aggressively refactor our codebase, it becomes more difficult to make changes and to maintain over time, slowing down the rate at which we can add new features"

## Adopt Trunk Based Development Practices
