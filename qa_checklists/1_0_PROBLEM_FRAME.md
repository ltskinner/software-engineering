# 1.0 - Problem Framing

* [ ] What type of problem is this?
  * [ ] Traditional software engineering?
  * [ ] Data engineering/transformation?  
  * [ ] Data science with a focus on statistical analysis/analytics?
  * [ ] Machine learning - straightforwards classification/regression?
  * [ ] Hardcore deep learning?
    * [ ] NER?
    * [ ] NRE?
    * [ ] QA?
    * [ ] RL?
    * [ ] etc...
    * [ ] New horizon?

## Data Engineering/Transformation Workflows

* [ ] Have properly mapped schemas of source data?
* [ ] Have properly mapped schemas of transformed data?
* [ ] Have ensured there are viable interfaces and libraries to interact with existing data?
* [ ] Have considered how the volume of data will affect architectural and system needs to process?
  * (If you have 1TB of shit, you cant process that in RAM - be prepared to plan accordingly)
* [ ] Determined interval at which the transformation needs to occur?
  * [ ] Have ensured infrastructure to perform transfer on said interval is feasible?
* [ ] Have ensured there is a viable interface to write and interact with data post transform?
* [ ] Have run a cost analysis of data at its desination?
* [ ] Have enumerated ways in which the data transform could fail?
* [ ] Have addessed each of the ways the data transform could fail?

## Data Science/Analytics Workflows

* [ ] Have you tried more transformations and visualizations than you could possibly hope to report on?
* [ ] Have you found a good framework or platform for displaying your results?
  * [ ] Excel charts?
  * [ ] Plotly charts --> reports?
  * [ ] Dash interactive apps?
* [ ] Have you selected visualizations that will be best recieved by your audience? (Audience > your reception)
* [ ] Have you visualized each result in multiple ways and selected the best?
  * [ ] Have you considered how colors will affect reception?
  * [ ] Have you considered how shape will affect reception?
  * [ ] Have you considered how size will affect reception?
  * [ ] Have you considered how relation to other data will affect reception?

## Machine Learning + Deep Learning Workflows

* [ ] Have listed initial techniques that will be used?
* [ ] Have researched more cutting edge techniques for the frame?
* [ ] Have determined the best layer to insert various models at?
  * (Have vision for a model harness that allows hot swapping different models for testing)
* [ ] Have compute resources required for training phatty models? (or have means of acquiring them?)
* [ ] Have enough time build into the estimate for Engineer to learn intracasies of model being used?
