# Chapter 15: Analyze Telemetry to better Anticipate Problems and Achieve Goals

"Given a herd of cattle that all look and act the same, which cattle look different from the rest? Or more concretely, if we have a thousand-node stateless compute cluster, all running the same software and sibject to the same approximate traffic load, our challence is to find any nodes that dont look like the rest of the nodes"

## Use Means and Standard Deviations to Detect Potential Problems

"Alert fatigue is the single biggest problem we have right now... We need to be more intelligent about our alerts or we'll all go insane"

## Instrument and Alert on Undesired Outcomes

* Only alert on measures that would have indicated an issue or failure had they been enabled
* Dont just use rules of thumb or best practice tools - reall understand what kind of things you want to be alerted on

## Using Anomaly Detection Techniques

* Use `smoothing` to get less dramatic charts
* Fast Fourier Transforms are also good
* So is the Kolmogorov-Smirnov filter
* Marketing and Business Intelligence people typically have good experience with time series stuff
