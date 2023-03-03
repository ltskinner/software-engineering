# Chapter 1. Data Engineering Described

## What is Data Engineering

### Data Engineering Defined

Data engineering is the development, implementation and maintenance of systems and processes that take in raw data and produce high-quality, consistent, information that supports downstream use cases, such as analysis and machine learning

Data engineering is the intersection of security, data management, DataOps, data architecture, orchestration, and software engineering.

A data engineer manages the data engineering lifecycle, beginning with getting data from source systems and engine with serving data for use cases, such as analysis or machine learning

### The Data Engineering Lifecycle

- generation
- storage
- ingestion
- transformation
- serving

`generation` -> `ingestion` -> `transformation` -> `serving` -> (analytics, ml, reverse ETL)

`storage` lives underneath ingestion, transformation, and serving

Underpinned by (at all stages):

- security
- data management
- dataOps
- data architecture
- orchestration
- software engineering

New generation systems were defined by:

- cost effectiveness
- scalability
- availability
- reliability

After lessons learned from monolith data warehouse systems

Three Vs of data:

- velocity
- variety
- volume

### Data Engineering and Data Science

"We believe data engineering is separate from data science and analytics. They complement each other, but are distinctly different."

- Data engineering sits upstream and provides inputs used by data scientists
- Data scientists convert these inputs into something useful

#### Data Science Hierarchy of Needs

- collect
  - instrumentation, logging, sensors, external data, user generated content
- move/store
  - reliable data flow, infrastructure, pipelines, etl, structured and unstructured data storage
- explore/transform
  - cleaning, anomaly detection, prep
- aggregate/label
  - analytics, metrics, segments, aggregates, features, training data
- learn/optimize
  - a/b testing, experimentation, simple ml algorithms
- ai, deep learning

lol 70-80% of time spent on low levels of data hierarchy (80/20 strikes again)

## Data Engineering Skills and Activities

The balancing act of data engineering:

- cost
- agility
- scalability
- simplicity
- reuse
- interoperability

Much of the best of breed tools these days abstract away low level stuff, so primary focuses now are:

- simplicity
- cost effect
- best services
- creating agile data structures that evolve with new trends

### Data Maturity and the Data Engineer

- `data maturity` - the progression towards higher data utilization, capabilityies, and integration across the organization

Data Maturity Models (DMM) - lots, but lets take a simplified view:

- 1. Starting with data
- 2. Scaling with data
- 3. Leading with data

### 1. Starting with Data

Goals:

- move fast
- get traction
- add value

Key things to focus on:

- Get buy-in from key stakeholders (like execs) and find sponsors for initiatives to `design and build` a data architecture to support the companies goals
- Define the right data architecture
  - determing a business goal or competitive advantage to achieve
- Identify and audit data that will support key initiatives and operate within the designed architecture
- Build a solid foundation for future data analysts and scientist
  - thing about reporting and modeling that will provide competitive value

Some tips:

- Get quick wins - without wins easy to lose steam and buyin
  - Its ok if this accumulates debt, but have a plan to reduce over time
- Get out and talk to people and avoid working in silos
  - Must get feedback and many different perspectives
- Avoid heavy lifting and boxing yourself in with unneccessary technical complexity
  - Use off the shelf turnkey solutions wherever possible

### 2. Scaling with Data

Primary challange is creating scalabale data architectures and planning for a future where the 🅱️ompany is **genuinely** data-driven

Goals:

- Establish formal practices
- Create scalable and robust data architectures
- Adopt DevOps and DataOps practices
- Build systems that support ML
- Continue to avoid heavy lifting and only customize when a competitive advantage results

Issues to watch for:

- Be hesitant to adopt bleeding edge tech based on "social proof"
  - Technology decisions should by driven by the value theyll deliver to your customer
- The main bottleneck is not cluster nodes, storage or technology - rather it is the `data engineering team` itself
  - focus on solutions that are simple to deploy and manage, and expand the teams throughput
- Dont be a technologist.
  - Lead and focus on communicating the practical utility of data
  - Teach the organization how to consume and leverage data

### 3. Leading with Data

Tasks:

- Create automation for seamless introduction of new data
- Focus on building custom tools and systems that leverage data as a competitive advantage
- Focus on the "enterprisey" aspects of data like data management, governance, quality, DataOps
- Deploy tools that expose and disseminate data throuought the organization (catalogues, data lineage tools, metadata management systems)
- Collaborate efficiently with software engineers, ML engineers, analysts, and others
- Create a community and environment where people can collaborate and speak openly, no matter their role or position

Issues to watch for:

- Complacency
  - focus on maintenance and improvement, or else risk falling back to a lower stage
- Technology distractions are a significant dancer
  - Dont pursue expensive hobby projects
  - Utilize custom-build technology only where it provides a competitive advantage

### The Background and Skills of a Data Engineer

### Business Responsibilities

- Know how to communcate with nontechnical and technical people
  - This means understanding org structures and power dynamics as well
- Understand how to scope and gather business and product requirements
- Understand the cultural foundations of Agile, DevOps, and DataOps
- Control costs
- Learn continuously

Success or failure is rarely a technology issue. Knowing how to navigate an organization, scope and gather requirements, control costs, and continuously learn are key descriminators.

### The Continuum of Data Engineering Roles, from A to B

In data science, there are:

- Type A - `analysis` - who focus on understanding and deriving insights from data
- Type B - `building` - who focus on making datascience work in production

For data engineers:

- Type A - `abstraction` - who keeps data architecture abstract and straightforward, using off the shelf products, managed services, and tools
- Type B - `build` - build data systems that scale and focus on exploiting competitive advantage

## Data Engineers Inside an Organization

### Internal-Facing vs External Facing

External facing:

- apps, iot devices, ecommerce, etc
- the data engineer architects, builds, manages the systems that collect, store, and process event data
- typically deal with much larger concurrency loads
- need to find ways to limit infrastructure impact of any single user
- security is a concern

Internal facing:

- focuses on needs of the business and internal stakeholders
- creating and maintaining data pipelines and data warehouses (that facillitate BI dashboards, reports, processes, ml models, etc)

### Data Engineers and Other Technical Roles

Basically, are the hub between `data producers` and `data consumers`

#### Upstream Stakeholders

- Data Architects
  - These guys design the blueprint for organizational data management
  - map out processes and overall data architecture and systems
  - serve as a bridge between an organizations technical and non technical folks
  - they also implement policies for managing data across silos and business units
  - steer global strategies for data management and governance
- Software Engineers
  - generate internal data
    - event data and logs
  - in well run orgs, software engineers and data engineers coordinate from inception to design app data for consumption by analytics and ml applications
    - work together to understand:
      - apps taht generate data
      - data volume
      - frequency
      - format
      - anything else (security, compliance)

#### Downstream Stakeholders

- Data Scientists
  - building `forward looking` models for predictions and recommendations
  - models are evaluated on live data
  - interesting: data scientists who work exclusively on a single workstation force themselves to downsample data, making preparation more complicated and possibly compromising quality of models
    - locally developed code is often cancer, and is lacking automation
  - **data engineers should help data scientists enable a path to production**
- Data Analysts
  - seek to understand business performance and trends
  - focus on `past and present`
  - often are domain experts in the data they work in
    - intimately familiar with data definitions, characteristics, and quality problems
  - their downstream customers are business users, management, and executives
- ML and AI engineers and researchers
  - MLOps is becoming large part of workflows

### Data Engineers and Business Leadership

#### Data in the C-Suite

- CEO
  - data engineers provide a window to whats possible with data
  - what data is available (internal and external) and the timeframe it is available
- CIO
  - Internally facing
  - posess deep knowledge of information technology and business processes
- CTO
  - Similar to CIO, but externally facing
  - Owns strategy and architectures for externally facing applications
- Chief Data Officer
  - Manage data as a business asset
  - oversee products, strategy, initiatives, and core functions
- Chief Analytics Officer
  - variant of CDO
  - more responsible for decision making
- Chief Algorithms Officer
  - highly technical role focused on data science and ml
  - on top of current research, set research agendas and build research teams

#### Data Engineers and Project Managers

"Business never sleeps"

Usually a long backlog of things the stakeholders want to address and new initiatives

- PMs need to filter and prioritize these asks

#### Data Engineers and Product Managers

### Reccomended books:

- Building Analytics Teams - John Thompson
- Data Teams - Jesse Anderson

Which cover frameworks and perspectives on:

- roles of executives with data
- who to hore
- how to construct the most effective data team for the company

"Companies dont hire engineers to simply hack code in isolation. To be worth of their title, engineers should develop a deep understanding of the problems theyre tasked with solving, the technology tools at their disposal, and the people they work with and serve"
