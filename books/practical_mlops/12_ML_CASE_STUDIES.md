# Chapter 12. ML Engineering and MLOps Case Studies

## Unileky Benefits of Ignorance in Building ML Models

Unlikely benefits to ignorance:

- courage to try something challenging (would have never tried if you knew how hard it was)

Impressive.

## MLOps Projects at Sqor Sports Social network

### Mechanical Turk Data Labeling

if 7/9 labelers agree on a sample, 99.9999% accuracy

## Critical Challenges in MLOps

### Ethical and Unintended Consequences

### Lack of Operational Excellence

### Focus on Prediction Accuracy vs the Big Picture

### Interview 1

3-5 most important things

- Model is relatively small piece inside a broader system when you productionalize it
  - but at same time, one of the most critical (if the model doesnt return satisfactory predictions, its all kinda pointless)
- Reality of deploying an ML system and observing users often breaks our assumptions, and so the process becomes iterative
- Data collection process is also extremely important

3-5 things for successful career

- learn to deal with the uncertainty associated with the ML dev process
- learn to work in cross-functional teams and people with little to no ML experiece
- create repeatable processes
- learn to put yourself in users shows
- strive to avoid technical debt

### Interview 2

3-5 most impoartant things

- important that people who understand the business collaborate closely with the mlops folks
  - must maintain constant interaction to understand experimentation
- manage your environments well
- sometimes will need to port a model into c++ for prod speed

3-5 things for successful career

- create reproducible ml pipelines
- capture the governance data for end-to-end ml lifecycle
- monitor ml applications for operational and ML-related issues

## Final Recommendations to Implement MLOps

- Start with small wins
- Use the cloud, dont fight the cloud
- Get you and your team certified on a cloud platform and an ML specialization
- Automate from the start of a project. An excellent initial automation step is CI of the project ("if it isnt automated, its broken")
- Practice Kaizen with your pipeline
- When dealing with large teams or big data, focus on using platform technology such as AWS sagemaker, amazon emr, azure ml studio
- Dont focus only on the complexity of techniques, i.e., deep learning vs solving the problem with any tool that works
- Take data governance and cybersecurity seriously. One way to accomplish this is by using enterprise support for your platform and having regular audits of your architecture and practice

Three Laws of Automation consider when thinking about MLOps:

- Any task that talks about being automated will eventually become automated
- If it isnt automated, its broken
- If a human is doing it, eventually a machine will do it better

## Security Concerns

### Data Governance and Cyber

Partial list of best practices:

- Use Principle of Least Priviledge
- Encrypt data at rest and in transit
- Assume systems that are not automated are insecure
- Use cloud platforms since they have a shared security model
- Use enterprise support and engage in quarterly architecture and security audits
- Train staff on platforms used by getting them certified
- Engage company in quarterly and yearly training on new technology and best practices
- Create a healthy company culture with standards of excellence, competent employees, and principled leadership

## MLOps Design Patterns

- CaaS
  - Container as a service
- MLOps Platform
  - Sagemaker, MLStudio
- Serverless
  - Lambda
- Spark-Centric
- Kubernetes-Centric

## Exercises

- [ ] Build a ML app as quickly as possible that is both continuously trained and continuously deployed
- [ ] Deploy a ML model using the k8s stack
- [ ] Deploy the same ml model using cd with aws, azure
- [ ] Create an automated security scan of the containers for a ML project using a cloud-native build system
- [ ] Train a model using a cloud-based AutoML system using a local AutoML system like CreateML or Ludwig

## Critical Thinking Discussion Questions

- How could you build a recommendation engine that doesnt have as many negative externalities as current social media reccomendation engines? What would you change, and how?
- What could be done to improve the accuracy and interpretability of modeling complex systems like nutrition, climate, and elections?
- How could operational excellence be the secret ingredient for a company wanting to be a ML technology leader?
- If operational excellence is a cruicial consideration for MLOps, what are your organizations hiring criteria to identify the right talent?
- Explain the role of operational excellence in ml concerning enterprise support for cloud computing? Does it matter, and why?
