# Kubernetes In Action

## Part 1. Overview

### [Chapter 1. Introducing Kubernetes](./1_1_INTRO_K8.md)

*kubernetes* is greek for pilot or helmsman

- abstracts away the hardware infrastructure and exposes the whole datacenter as a single enormous computational resource **POG**

**NoOps**: Ideally you want the developers to deploy the application themselves without knowing anything about the hardware infrastructure and without dealing with the ops team

Docker is a platform for packaging, distributing, and running applications

- Images:
- Registries:
- Containers:

Does **NOT** provide process isolation - actual isolation done at the linux kernel level via namespaces. Docker just makes it easy to use those features

K8 Clusters:

- *master* node
  - hosts the *Kubernetes Control Plane* that controls and manages the whole K8 system
  - Components:
    - The *K8 API Server*, which you and the other Control Plane components communicate with
    - The *Scheduler*, which schedules you apps (assigns a worker node to each deployable component of your application)
    - The *Controller Manager*, which performs cluster-level functions, such as replicating components, keeping track of worker nodes, handling node failures, and so on
    - *etcd*, a reliable distributed data store that persistently stores the cluster configuration
- worker *nodes* that run the actual applications you deploy
  - Docker, rkt, or another *container runtime* which runs your containers
  - The Kubelet, which talks to the API server and manages containers on its node
  - The *K8 Service Proxy* (kube-proxy), which load balances network traffic between application components

Running an Application in K8s

To run:

- need to package into one or more container images
- push those images to an image registry
- then post a description of your app tot the k8 api server

The description includes info like:

- container image or images that contain your application components
- how those components are related to each other
- which ones need to be run co-located, and which dont
- for each component, can specify how many copies (replicas) you want to run
- which components provide a service to either internal or external clients and should be exposed through a single IP address tomake discoverable
