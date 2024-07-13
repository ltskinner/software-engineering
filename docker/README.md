# Docker Commands

## Basic Workflow

* 1. Define `Dockerfile`
* 2. `build` Dockerfile into **image**
* 3. `run` image as **container**

## Defining Dockerfiles

```dockerfile
FROM ubuntu:18.04

RUN sudo apt-get update

RUN pip install pandas
```

## Building Dockerfiles into Images

Save the Dockerfile in a folder like this:

```
/your_project
  /data
  /codebase
  /docker
    Dockerfile  # yes this is the filename, no extension
```

Next, to be safe, `cd docker` into the docker folder and run

`docker build . --tag <image_name>:<tag>`

Note:

* Dont forget the . at the end
* The `<tag>` can be likened to a `version` of the image

## Running Images as Containers

### Flags

* `-i` - Interactive container
* `-t` - Launch with terminal
* `-p <machine_port>:<container_port>` - expose port to machine

### Basic -> interactive terminal

`docker run -i -t -p 8888:8888 <image_name>:<tag>`

## Utility

See all images:

`docker image ls`
