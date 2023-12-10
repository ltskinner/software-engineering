# Gremlin

## Install

[https://tinkerpop.apache.org/download.html](https://tinkerpop.apache.org/download.html)

## Docker

docker pull tinkerpop/gremlin-server
docker pull tinkerpop/gremlin-console

### Python

`activate gremlin39`

pip install gremlinpython
pip install tornado

## CMDs

[https://tinkerpop.apache.org/docs/3.4.2/reference/](https://tinkerpop.apache.org/docs/3.4.2/reference/)

Start Server:

`docker run --rm -p 8182:8182 tinkerpop/gremlin-server`

Start Console:

`docker run -it tinkerpop/gremlin-console`

Exit Console:

`:exit`

Run Script:

`docker run -it -v ./gremlin.groovy:/scripts/gremlin.groovy tinkerpop/gremlin-console -e /scripts/gremlin.groovy`


### Example

docker run -it -v ./ch3.groovy:/scripts/ch3.groovy tinkerpop/gremlin-console

:load /scripts/ch3.groovy
