# Chapter 7. Responsible AI

Stakeholders:

- Model builders
  - Data scientists and ML researchers directly involved in building ML models
- ML Engineers
  - Members of the MLOps teams directly involved in deploying ML models
- Business decision makers
  - Decide whether or not to incorporate the ML model into their business processes or customer-facing applications and will need to evaluate whether the model is fit for this purpose
- End users of ML systems
  - Make use of predictions from an ML model
    - customers, emplyees, hybrids
- Regulatory and compliance agencies
  - Financial audirots, government agencies, governance teams

## Design Pattern 28: Heuristic Benchmark

Compares a ML model against a simple, easy-to-understand heuristic in order to explain the models performance to business decision makers

Is an accuracy of XX% good in the business context?

Good bet is to compare it against existing production systems, but if this doesnt exist, gotta create a heuristic

- easy to understand
- relatively trivial to compute

Good examples:

- constants
- rules of thumb
- bulk stats (mean, median, mode)

| Scenario | Heuristic Benchmark | Example Task | Implementation for Example Task |
| - | - | - | - |
| Regression problem where features and interactions between features are not well understood by the business | Mean or median value of the label over the training data. Choose the median if there are a lot of outliers | Time interval before a question on stack overflow is answered | Predict that it will take 2120 seconds always. 2120 is the median time to afirst answer over the entire training dataset |
| Binary classification problems where features and interactions between features are not well understood by the business | Overall fraction of positives in the training data |  whether or not an an accepted answer in stack overflow will be edited | Predict .36 as that is the output probability for all answers |
| Multilabel classification problem where features and interactions between features are not well understood by the business | Distribution of the label value over the training data | Country from which a stack overflow question will be answered | Predict .003 for france, .08 for india, and so on |
| Regression problem where there is a single very important, numeric feature | Linear regression based on what is, intuitively, the single most important feature | Predict taxi fare amount given pickup and dropoff locations. The distance between the two points, is intuitively, a key feature | Fare is $4.64 per km, so the fare is based purely off the kms |
| Regression problem with one or two important features. The features could be numeric or categorical but should be commonly used heuristics | Lookup table where the rows and columns correspond to the key feature (should be discretized if necessary) and the prediction for each cell is the average label in that cell estimated over the training data | Predict the duration of bycicle rental. Here, the two key features are the station that the bike is from and whether or not it is peak commuting hours | Lookup table of average rental duration from each station based on peak hour vs non-peak |
| Classification problem with one or two important features. The features could be numeric or categorical | As above, except that the prediction for each cell is the distribution of labels in that cell. If the goal is to predict a single class, compute the mode of the label in each cell | Predict whether a stack overflow question will get answered within one day. The most important feature here is the primary tag | For each tag, compute the fraction of questions that are answered within one day |
| Regression problem that involves predicting the future value of a time series | Persistance or linear trend. Take seasonality into account. For annual data, compute against the same day/week/quarter of previous year | Predict weekly sales volume |  |
| Classification problem currently being solved by human experts. This is common for image, video, and text tasks and includes scenarios where it is cost-prohibitive to routinely solve the problem with human experts | Performance of human experts | Detecting eye disease from retinal scans | Have three or more physicians examine each image. Treat the decision of a majority of physicians as being correct, and look at the percentile ranking of the ML model among human experts |
| Preventeteive or predictive maintenance | Perform maintenance on a fixed schedule | Preventative maintenance of a car | Bring cars in for maintenance every 3 months. The 3 month median time to failure of cars from last service date |
| Anomaly detection | 99th percentile value estimated from the training dataset | Identiy dos atatck from network traffic | Find 99th percentile of the number of requests per minute in the historical data. If over any one-minute period, the number of requests exceeds this number, flag it as a dos attack |
| Recommendation model | Recommend the most popular item in the category of the customers last purchase | Recommend movies to users | If a user just saw (and liked) Inception (a sci-fi movie), recommend Icarus to them (the most popular sci-fi movie they have not yet watched) |

May sometimes require special data collection

Also, after constructing the naive heuristic, need to make sure that the models perfomance justifies its existence

## Design Pattern 29: Explainable Predictions

Increases user trust in ML system by providing users with an understanding of how and why models make certain decisions

Be careful about coefficients - because model features are not the same unit and scale, the pure coefficients can be misleading. Coefficients also dont tell us anything about the relationship between features

Two types of feature attributions:

- Instance-level
  - Feature attributions that explain a models output for an individual prediciton
- Global
  - Analyze models behavior across an aggregate to draw conslusions about how the model is behaving as a whole

Check out:

- Sampled Shapely
  - Based on the concept of Shapely Value, this determines a features marginal contribution by calculating howmuch adding and removing that feature affects a prediction, analyzed over multiple combinations of feature values
- Integrated Gradients (IG)
  - Using a predefined model baseline, IG calcualtes the derivatives (gradients) along the path from this baseline to a specific input

### Model Baseline

The thing we compare attribution values against:

- informative
  - compare a prediction with a specific alternative scenario
- uninformative
  - typically compare against some average case across a training dataset

Some libraries:

- SHAP
- XRAI

## Design Pattern 30: Fairness Lens

Suggests the use of preprocessing and postprocessing techniques to ensure that model predicitons are fair and equitable for different groups of users and scenarios

### Before Training

Differnt types of data bias:

| Type | Definition | Considerations for Analysis |
| - | - | - |
| Data distribution bias | Data that doesnt contain an equal representation of all possible groups that will use the model in production | Does the dataset contain a balanced set of examples across all relevant demographic slices (gender, age, race, religion, etc). does each label in the data contain a balance split of all possible variations of this label? |
| Data representation bias | Data that is well balanced, but doesnt represent different slices of data equally | For classification models, are labels balanced across relevant features? For example, in a dataset inteded for credit worthiness prediction, does the data contain an equal representation across gender, race, and other identity characteristics of people marked as unlikely to pay back a loan? Is there bias in the way different demographic groups are represented in the data? This is especially relevant for models predicting sentiment or a rating value. Is there subjective bias introduced by data labelers? |

### Allow and Disallow Lists

When we cant find a way to fix inherent bias in our data or model directly, its possible to hardcode rules on top of our model using allow and disallow lists

This applies mostly to classification or generative models, where there are labels or words we dont want our model to return

Can be applied at two levels:

- Data collection
- After training
  - Basically a filter to make sure no unsavory shit gets returned to the user lmao

Can also do data augmentation, or ablation, basically remove or replace terms in the training dataset HAHA COWBOY
