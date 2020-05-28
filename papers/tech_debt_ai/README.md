# Hidden Technical Debt in Machine Learning Systems

"Not all debt is bad, but all debt needs to be serviced"

[https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)

## How to Pay Off Technical Debt

* `Refactoring` code
* Improving `unit tests`
* Deleting `dead code`
* Reducing `dependencies`
* Tightening `APIs`
* Improving `documentation`


## Primary Issues

* Models erode abstraction boundaries unknowingly ("silently")
* Attempted reuse or chaining of input signals may couple otherwise disjoint systems
* Black box treatment of models results in troves of "glue code" aka `calibration layers` - I LOVE this term
  * These lock in assumptions
* Changes in the external workd may have unintended consequences
* Monitoring models can be incredibly difficult as well

## 2) Complex Models Erode Boundaries and Abstractions

* **CACE:** Changing Anything Changes Everything
  * Input signals
  * Hyperparameters
  * Learning settings
  * Sampling methods
  * Convergence thresholds
  * Data selection
  * Like any tweak made to the system
* **Entaglement**
  * Because signals get mixed together, these entaglements result systems whos features are hard to isolate and improve
  * "No inputs are ever really independent"
  * **Solution:** Isolate models and serve `ensembles`
* **Undeclared Consumers**
  * Other models and features of a system that depend on an expected output are high in debt
  * Unexpected changes in the current model results in bad downstream consequences

## 3) Data Dependencies Cost More than Code Dependencies

* **Unstable Data Dependencies**
  * Version your data
  * Changes could occur to the source at any time, and you need to be able to roll back
* **Underutilized Data Dependencies**
  * Sometimes, something is used, but it doesnt actually improve the system
  * This same dependecy, were it to change, could be catastrophic
  * REMOVE these dependencies because they are high risk and low reward
  * These creep in via:
    * Legacy features (things made obsolete by newer better features)
    * Bundled features (things that come in groups, including features that are not very useful)
    * eps-Features (things added that marginally improve the model, but at the cost of high complexity)
    * Correlated Features (two features that are correlated, but only one actually drives the model)
  * --> Perform **"Static Analysis of Data Dependencies"**
    * Look at the code dependency graphs made by compilers

## 4) Feedback Loops

* Two Types:
  * Direct Loops
  * Hidden Looks - anything coming back from an environment that a model is operating in
* Leverage bandit systesm to ensure models arent cheating
  * Corner off parts of input data and ensure they are not affected by any past model
* Live models have the potential to infulence the selection of its own future training data

## 5) ML-System Anti-Patterns

* **Glue Code** - `calibration layers`
  * Huggingface :)
* **Pipeline Jungles**
  * Wild preprocessing pipelines
    * Scrapes
    * Joins
    * Sampling
    * Intermediate output files
  * Indicative of no separation between `research` and `engineering`
* **Dead Experimental Codepaths**
  * Get rid of these
  * Clean up and minimize branches
  * Focus on `trunk dev`
* **Standard Abstractions (lack of)**
  * The way all relational database have the same level of abstraction
    * This does not exist for ML
  * How can we better abstract? Safe trusting development ecosystems
* **Common Smells**
  * **Plain-Old-Data Smell**
    * When the data used to train a model does not have its own host of metadata
      * If raw `floats` and `ints` are being used, these numbers are essentially unitless
      * SHOULD know whether its a:
        * Multiplier
        * Decision threshold
        * etc
    * Predicted data should also include info on what the prediction is
      * AND how it should be used
  * **Multiple Language Smell** - Stick to one language
  * **Prototype Smell**
    * You know one when you see one
    * Keep these alive for as short as possible
    * Results at small scale rarely reflect reality at full scale

## 6) Configuration Debt

"We have observed that both researchers and engineers may treat configuration (and extension of configuration) as an afterthought"

* It should be easy to specify a configuration as a `small change` from a previous config
* It should be hard to make manual errors, omissions, or oversights
* It should be easy to see, visually, the difference in the configuration between two models
* It should be easy to automatically assert and verify basic facts about the configuration:
  * Number of features used
  * Transitive closure of data dependencies
  * etc
* It should be possible to detect unused or redundant settings
* Configurations should undergo a full code review and be checked into a repo

## 7) Dealing with Changes in the External World

* **Fixed thresholds in Dynamic Systems**
  * These thresholds MUST be determined manually or else youre fucked
  * Use validation hold out data to figure these out
* **Monitoring and Testing** - What to Monitor?
  * Prediction Bias:
    * Watch distribution of predictions
    * If distribution of predictions change dramatically, something in real world data is also changing
  * Action limits
    * If the model does something, set boundaries that require notifications to do so
  * Up-Stream Producers
    * For data coming inbound, need to make sure thos eproducers are being monitored

## 8) Other Areas of ML-Related Debt

* **Data Testing Debt**
  * "If data replaces code in ML systems, and code should be tested" then input data should be tested
  * Focus mainly on distributions
* **Reproducibility Debt**
  * **MUST** be able to re-run experiments and have them be reproduced
* **Process Management Debt**
  * Configuration redistribtuion - to multiple models that make up a system
  * Management and assignment of resources to models with different business priorities
  * Need to be able to visualize and detect blockages in the flow of data in production pipelines
  * Develop tools to help recover from production failures
  * Anything that requires `manual` setup is a nono
* **Cultural Debt**
  * Reward:
    * Deletion of Features
    * Reduction of Complexity
    * Improvements of Reproducability
    * Improvements of Stability
    * Improvements of Monitoring
  * **HAVE TO MOVE PAST ACCURACY AS THE REWARD**

## 9) Conclusions: Measuring debt and paying it off

Ask yourself:

* How easily can an entirely new algorithmic approach be tested at full scale?
* What is the transitive closure of all data dependencies?
* How precisely can the impact of a new change to the system be measured?
* How does improving one model (or signal) degrade others?
* How quickly can new members of the team be brought up to speed?

"A research solution that only provides a small accuracy benefir at the cost of massive system complexity are bad"
