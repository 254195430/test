# MongoDB Dockerfile
# Pull base image.
FROM ubuntu:16.04
MAINTAINER Manish Sethi<manish@sethis.in>
# Install MongoDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys D68FA50FEA312927  && \
  echo 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse' > /etc/apt/sources.list.d/mongodb.list && \
  rm -fR /var/lib/apt/lists/*  && \
  mkdir /var/lib/apt/lists/partial  && \
#  echo 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse' > /etc/apt/sources.list.d/mongodb.list && \
  apt-get update && \
  apt-get -y install apt-transport-https  && \
  apt-get install -y mongodb-org && \
  rm -rf /var/lib/apt/lists/*
 
# Define mountable directories.
VOLUME ["/data/db"]
 
# Define working directory.
WORKDIR /data
 
# Define default command.
CMD ["mongod"]
 
# Expose ports.
EXPOSE 27017
EXPOSE 28017

