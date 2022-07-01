# Chapter 2. First Steps with Docker and K8s

## 2.1 Creating, Running, and Sharing a Container Image

Section covers:

- 1. Install Docker and run first "Hello world" container
- 2. Create trivial Node.js app that will later be deployed to Kubernetes
- 3. Package the app into a container image so you can then run it as an isolated container
- 4. Run a container based on the image
- 5. Push the image to Docker Hub so that anyone anywhere can run it

### 2.1.1. Installing Docker and running a Hello World Container

#### Running a Hello World Container

```
$ docker run busybox echo "Hello world"
$ docker run <image>
$ docker run <image>:<tag>
```

#### Understanding What Happens Behind the Scenes

#### Versioning Container Images

All software packages get updated, so more than a single version of a package usually exists

Docker supports having multiple versions or variants of the same inage under the same name

- this is done by having `unique tags`
- when referring to images without explicitly specifying the tag, Docker assumes you are referring to the `latest` tag

### 2.1.2. Creating a trivial node.js app

- build a trivial node.js app
- package it into a container image
- app will accept HTTP requests
- will respond with hostname of the machine its running on
  - this will show that the app is running inside a container and has its own host, not the host machine

[See app.js source](./2_1_node_js_app/app.js)

You **could** now download and install Node.js and test app directly, but this isnt necessary, because youll use Docker to package the app into a container image and enable it to be run anywhere without having to download or install anything (except Docker lel)

### 2.1.3. Creating a Dockerfile for the image

First, gotta create a `Dockerfile` - contains a list of instructions that docker will perform when building the image

- Dockerfile needs to be in the same directory as the app.js file

```Dockerfile
FROM node:7

ADD app.js /app.js
ENTRYPOINT ["node", "app.js"]
```

- FROM defines the container image youll use a starting point - node tag 7
- ADD adds the app.js from the local directory into the root dir of the image under the same name
- finally, define the command that should be executed when somebody runs the image
  - command is `node app.js`

#### Choosing a base image

- gotta contain a `node` binary executable

### 2.1.4. Building the container image

```
$ docker built -t kubia .
```

- here, telling docker to build an image called `kubia` based on the contents of the current directory

Tip: dont include any unnecessary files in the build directory, because theyll slow down the build process - especially when the Docker daemon is on a remote machine

#### Understanding Image layers

A image isnt a single, big, binary blob - rather it is composed of multiple layers

- re: the `complete` lines you see after pulling

#### Listing locally stored images

```
docker images
```

#### Comparing Building Images with a Dockerfile vs Manually

Can manually build image by running a container from an existing image, executing comands in the container, exiting the container, and committing the final state as a new image

- this is the process that running a Dockerfile does
  - except its [automatic. still is](https://www.youtube.com/watch?v=Kwm52hSCtuw)

### 2.1.5 Running the container image

```
$ docker run --name kubia-container -p 8080:8080 -d kubia
```

- tells Docker to run new container called `kubia-container`
- the container will be detached from the console `-d`, aka will run in background
- `-p` means port 8080 on the local will be mapped to port 8080 inside the container - acces thru http://localhost:8080

If on Mac or Windows, will need hostname or IP of VM instead of localhost

- look up with `DOCKER_HOST` env var

Woahh poggers actually didnt need this lol

#### Listing All Running Containers

```
$ docker ps

# Getting additional info about a container
$ docker inspect <container-name>
```

### 2.1.6 Exploring the inside of a running container

#### Running a Shell Inside an Existing Container

The node.js image on which youve based your image contains the bash shell,so can run the shell inside the container like this:

```
$ docker exec -it <container-name> <command>
$ docker exec -it kubia-container bash
```

#### Understanding that processes in a container run in the host os

#### The containers filesystem is also isolated

Tip: Entering a running container like this is useful when debugging an app running in a container

### 2.1.7 Stopping and removing a container

```
# stop
$ docker stop kubia-container

# remove a container
$ docker rm kubia-container
```

### 2.1.8 Pushing the image to an image registry

before pushing, need to re-tag image according to docker-hubs rules

```
# re-tag
$ docker tag kubia docker_hub_id/kubia

$ docker push docker_hub_id/kubia
```

This doesnt rename the tag, it creates an additional tag for the same image

#### Running the Image on a Different Machine

After the push to docker hub, the image will be available to everyone

```
$ docker run -p 8080:8080 -d docker_hub_id/kubia
```
