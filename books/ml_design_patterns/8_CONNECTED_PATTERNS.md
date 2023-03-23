# Chapter 8: Connected Patterns

## Pattern Interactions

## Patterns Within ML Projects

### ML Life Cycle

- Begins with clear understanding of the business goals
- Ultimately leads to having a ml in production that benefits that goal

Failure to complete any stage results in complete failure

- Define Business Use Cases
- Data Exploration
- Select Algorithm
- Data Pipeline Feature Engineering
- Build ML Model
- Evaluate
- Present Results
- Plan for Development
- Operationalize Model
- Monitor Model

For Corporate organizations, success is governed by factors more closely tied to the business:

- Improving customer retention
- Optimizing business processes
- Increasing customer engagement
- Decreasing churn rates

Creating well defined KPIs at the onset of an ML project can help to ensure that everyone is aligned on the common goal

ML is not the answer to all problems, and sometimes a rule-based heuristic is hard to beat

### Deployment Questions

- How should model retraining be managed?
- Will input data need to stream in?
- Should training happen on new batches of data or in real time?
- What about model inference? Should we plan for one-off batch inference jobs each week, or do we nee to support real-time prediction
- Are there special throughput or latency issues to consider?
- Is there a nmeed to handly spiky workloads?
- Is low latency a priority?
- Is network connectivity an issue?

## AI Readiness

### Tactical Phase: Manual Development

- Orgs first beginning to explore potential for AI to deliver, with a focus on short term projects
- Focus on proof of concepts or prototypes
- Typically, no process to scale solutions consistently, and ml tools are developed on an ad hoc basis

### Strategic Phase: Utilizing Pipelines

- Orgs have aligned AI efforts with business objectives and priorities, and ml is seen as a pivotal accelerator for the business
- Data pipelines for developing ML models are automated utilizing a fully managed, serverless data service for ingestion and processing and are either scheduled or event driven
- ML workflow for training, eval, and batch prediction is managed by an automated pipeline so that the stages of the ML lifecycle are executed by a performance monitoring trigger

### Transformational Phase: Fully Automated Processes

- Actively using ai to stimulate innovation, support agility, and cultivate a culture where experimentation and learning is ongoing
- Common to have product specific AI teams embedded into the broader product teams and supported by the advanced analytics team
- Reused datasets and ml assets
- Standardized ml feature stores
- Collaboration is easy and encouraged

## Common Patterns by Use Case and Data Type

### Natural Language Understanding

Common patterns:

- Embeddings
- Hashed Feature
- Neutral Class
- Multimodal Input
- Transfer Learning
- Two-Phase Predictions
- Cascade
- Windowed Inference

### Computer Vision

- Reframing
- Neutral Class
- Multimodal Input
- Transfer Learning
- Embeddings
- Multilabel
- Cascade
- Two-Phase Predictions

### Predictive Analytics

- Feature Store
- Feature Cross
- Embeddings
- Ensemble
- Transform
- Reframing
- Cascade
- Multilabel
- Neutral Class
- Windowed Inference
- Batch Serving

#### IoT Specific

- Feature Store
- Transform
- Reframing
- Hashed Feature
- Cascade
- Neutral Class
- Two-Phase Predictions
- Stateless Serving Function
- Windowed Inference

### Recommendation Systems

One of the most widespread applications of ml in business and often arise whenever users interact with items

- Embeddings
- Ensemble
- Multilabel
- Transfer Learning
- Feature Store
- Hashed Feature
- Reframing
- Transform
- Windowed Inference
- Two-Phase Predictions
- Neutral Class
- Multimodal Input
- Batch Serving

### Fraud and Anomaly Detection

- Rebalancing
- Feature Cross
- Embeddings
- Ensemble
- Two Phase Predictions
- Transform
- Feature Store
- Cascade
- Neutral Class
- Reframing