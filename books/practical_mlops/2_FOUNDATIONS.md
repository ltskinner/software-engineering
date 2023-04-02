# Chapter 2. MLOps Foundations

"Having a solid foundation to build on is critical to any technical endeavor"

## Bash and the Linux Command Line

Better way to think about the terminal is the "advanced settings" of the environment you are working on: the cloud, ml, or programming - if you need to do the advanced tasks, it is the way to perform it

## Cloud Shell Development Environments

If you use AWS CloudShell, good idea to edit the ~/.bashrc to customize the experience

Should learn vim

Cloud9 is also good because it allows you to make web requests form the console to deployed services, and has deep integration with AWS Lambda

## Bash and Shell Commands

A couple of immediately valuable things to do:

- install vim configs - `awesome vim`
- install ZSH configs - `ohmyzsh`

Commands:

- List Files
  - `ls -l`
- Run Commands
  - To find the location of executables
  - `which ls`
- Pipe operator
  - accepts the input form another command
- Files and Navigation
  - pwd
  - cd
- Input/Output
  - echo "foo bar baz" > out.txt
  - cat out.txt | wc -c
  - cat out.txt | wc -w
- Configuration
  - for ZSH start w `.zshrc`
  - for bash start w `.bashrc`
  - in here, can alias things
    - `alias flask-azure-ml="/somepath/flask-ml-azure-serverless && source ~/.flask-ml-azure/bin/activate"`
    - `export AWS_SECRET_ACCESS_KEY="<key>"`
    - `export AWS_ACCESS_KEY_ID="<key>"`
    - `export AWS_DEFAULT_REGION="us-east-1"`
    - these small investments pay big dividends as you build automation into your regular workflows
- Writing a Script

## Cloud Computing Foundations and Building Blocks

## Getting Started with Cloud Computing

## Python Crash Course

## Math for Programmers Crash Course

### Descriptive Statistics and Normal Distributions

### Optimization

### Machine Learning Key Concepts

### Doing Data Science

### Build an MLOps Pipeline from Zero

## Exercises

- [x] Do Build an MLOps Pipeline from Zero
- [x] Run a hello world python GitHub project and check it out and run your tests on all three clouds:
  - [x] AWS
  - [x] Azure
  - [x] GCP
- [x] Make a new flask application that serves out a "hello world" type route using AWS Elastic Beanstalk you think other people would find helpful
  - [x] PRIVATE REPO
  - [x] Put the code into a GitHub repo
  - [x] Create a CD process to deploy the Flask app using AWS codebuild
  - [x] Put a screenshot of it serving out a request in the README
- [ ] Fork this Flask ml app: https://github.com/paiml/practical-mlops-book/blob/main/README.md#chapter-2-mlops-in-the-cloud
  - [ ] Deploy it with CD on aws using elastic beanstalk and code pipeline
- [ ] Fork this Flask ML app: https://github.com/paiml/practical-mlops-book/blob/main/README.md#chapter-2-mlops-in-the-cloud
  - [ ] Deploy with on GCP with Google App engine and Cloud Build (or Cloud Run and Cloud Build)
- [ ] Fork this flask ML app: https://github.com/paiml/practical-mlops-book/blob/main/README.md#chapter-2-mlops-in-the-cloud
  - [ ] Deploy it with CD on Azure using Azure App Services and Azure DevOps Pipelines
- [ ] Use the traveling salesman code example and port it to work with coordinates you grab from an api
  - [ ] Say all of the best resturaunts in a city you want to visit
- [ ] Using TensorFlow Playground:
  - [ ] Experiment with changing the hyperparameters across different datasets as well as problem types
  - [ ] Can you identify optimal configurations of hidden layers, learning rate, and regularization rate for different datasets?

## Critical Thinking Discussion Questions

### 1 - these are long prompts lol

A company specializing in GPU databases has a key technical member advocating they `stop` using the cloud because it would be much more practical to buy their GPU hardware since they run it 24/7. This step would also allow them to get access to specialized GPUs much more quickly than they are available. On the other hand, another critical technical member who has all of the AWS certifications has promised to get him fired if he dares to try. He claims that they have already invested too much into AWS. Argue for or against this proposal

For buying own gpus: like if youre a 99th percentile gpu user, genuinely running GPUs 24/7, how is that any different from what cloud providers offer? Like if you run a gpu enough to where hardware failure is a discussion point its probably ok to invest in your gpus. However, that said, like this is just two people with different opinions - technical leaders dont make these decisions, the influence them. The project manager and money bugs need to get involved and do an analysis of cost like its just an optimization problem

For sticking to AWS: first off, lets address the interpersonal issue. The pAsSiOn of the aws bro to get his adversary fired is admirable and you want people who care that much, but thats also like kinda shitty to get someone fired for having a different opinion. You can posess all that same deranged energy without expending it. It looks like the key point of his argument is that investments in the past are locking the team into aws. Here, again, you want to run the numbers, but there is an x factor that is a bit more challenging to quantify which is all the automations and the fact that the team is probably pretty slick with aws by now. Switching to on prem gpus would likely require reskilling the dev teams which would def be a pain, but not unmanageable.

Personally, I think the solution is to do a prototype. Still do the financial analysis and make sure that its not completely rere to invest in their own gpus, and likewise that sticking with aws also wont sink them. Then, invest enough to get enough gpus and the technical knowhow to have an honest trial of prem gpus, define some kpis, measure the shit out of both teams, and see what comes out the other side. Theres difficult to quantify unknowns of both routes and we should get more data before going whole hog either direction

### 2 - long boi

A "Red Hat Certified Engineer" has built one of the most successful data centers in the southeast for a company with only 100 employees. Even tho the company is an e-commerce company, and not a cloud company, he claims this gives the company a huge advantage. On the other hand, a "google certified achitect" and "duke data science masters" graduate claims the company is in a risky position by using a data center they own. They point out that the company keeps losing data center engineers for google and has no disaster recovery plan or fault tolerance. Argue for or against this proposal

yeah i hate to play the quantify card again, but like what are the costs of operating their own datacenter vs moving the same functionality to the cloud. Like its no surprise that people with certifications from corporations that make money off people liking and using their products are arguing on behalf of the systems their certs come from haha like thats fine, but call a spade a spade

Operationally, how many data center engineers are we losing? and how hard is it to replace and upskill them? and if there is truly no disaster recovery plan or fault tolerance, those are huge (and mitigateable) risks. Furthermore, as an ecommerce platform, like theoretically they could serve customers wherever - how are the response times and reliability of connections to users across the US? across the world? one data center in the southeast might be great for people nearby but not others

The decision here is not one to be made by developers, the C suite needs to do this. What are the companies growth plans? If the company plans to go nationwide or international, how much of their present datacenter infrastructure and architecture and processes are actually scalable to another "unit" somewhere else? Plus, this one red hat engineer bro like what if he leaves? You cant build an organization around heros, and like theres too many bottlenecks for this company to scale to anything larger

BUT, that said, like if the company is fine staying regional and 80% of their consumers are happy with service, figure out how to make current assets in the datacenter work. Its not the end of the world but maintaining is a very different headspace than growing

### What are the key technical differences between AWS Lambda and AWS Elastic Beanstalk

Lambda is serverless and the dankest for small jobs and event driven stuff

Elastic Beanstalk is like a server server

Compute environment wise, safe to assume they are identical, the only real difference is the serverless vs servered paradigm, and which is better depends entirely on your use case

### Why would a managed file service like EFS or Google Filestore be helpful in a real-world workflow in corporate America?

Im not sure if this is a 100% informed assessment, but based on googling around it seems like efs and google filestore are functionally equivalent dropbox and onedrive for a naive user just wanting to save like word docs n stuff. The big value add here is the interfacability to other aws or gcp services, and that you can have all your true files easily accessible at the human level, and the machine level. One of the big issues I see today is nontechnical folks with office docs that like the best tool they have to transfer and share is email or box, neither of which integrate directly (easily) to the cloud, so theres always some hassleware that needs to get built if you wanna automate recieving or delivering anything to nontechs

### Kaizen starts with a simple question: can we do better? if so, what should we do to get better this week or today? Finally, how can we apply Kaizen to our ML projects?

![](https://browsecat.art/sites/default/files/consciousness-wallpapers-103583-718865-787819.png)
