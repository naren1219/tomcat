#!/bin/bash
set -e

BASEDIR=$(dirname $0)

# login to private docker registry
IMAGE=749833379596.dkr.ecr.us-east-1.amazonaws.com/genospace/tomcat7

jar -xvf VN_sample.war

eval $(aws ecr get-login --region us-east-1 --no-include-email)

# Build the app image:
sudo docker build --force-rm=true -t $IMAGE:$VERSION .

# Push both images
docker push $IMAGE:$VERSION
