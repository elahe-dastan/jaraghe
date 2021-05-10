# jaraghe

I use this project to learn Spark and newer technologies, this is not in code 101 because I usually come back to the 
codes and file like this and finding a repository is much easier than finding a file in a big repository.

# Install and Run Spark
I think downloading and installing anything that can be used by a docker container is not wise so here's what I did: <br/>
```shell
docker pull bitnami/spark
docker run bitnami/spark
docker exec -it [docker-name] /bin/bash
./bin/pyspark
```