# Chapter 1. The Need for Machine Learning Design Patterns

- Design Patterns capture best practices an solutions to commonly occuring problems
- They Codify the knowledge and experience of experts into advice that all practitioners can follow

## Machine Learning Terminology

### Models and Frameworks

### Data and Feature Engineering

### The Machine Learning Process

- training
- evaluation
- serving
- prediction/inference
	- online prediction
	- batch prediction

### Data and Model Tooling

### Roles

- Data Scientist
	- Someone focused on collecting, interpreting, and processing datasets
	- Statistical and exploratory analysis
	- Collection, feature engineering, model building
- Data Engineer
	- Infrastructure and workflows powering an organizations data
	- Ingest data, data pipelines, and how data is stored and transferred
- ML Engineers
	- Takemodels developed by data scientists, and manage infrastructure and operations around training and deploying thos models
	- Build production systems to handle updating models, model versioning, and serving predictions to end users
- Research Scientists
	- Finding and developing new algorithms to advance the discipline of ML
	- Most time spent prototyping and evaluating new approaches to ML, rather than building out production systems
- Data Analysts
	- Evaluate and gather insights from data, then summarize these insights for other teams within the org
- Developers
	- In charge of building production systems that enable end users to access ML models
	- Utilize model serving infrastructure implemented by ML Engineers to build applications and user interfaces for surfacing predictions to model users

## Common Challanges in Machine Learning

### Data Quality

ML models are only as reliable as the data used to train them

- Accuracy
- Completeness
	- The "world view" of your model as a result of the data
- Consistency
	- Develop set of standards for the labeling process
- Timeliness
	- The latency between when the event occured and when it was added to your db

### Reproducability

Several artifacts need to be fixed:

- the data used
- the splitting mechanism to generate datasets for training and validation
- data preparation and model hyperparameters
- variables like batch size and learning rate schedule

Also be aware that different versions of frameworks will have different random seeds baked into underlying components

### Data Drift

The challenge of ensuring the ml models stay relevant, and that model predictions are an accurate reflection of the environment in which theyre being used

Important to continually:

- update your training dataset
- retrain your model
- modify the weight your model assigns to particular groups of input data

## Scale

Of both training and inference data
