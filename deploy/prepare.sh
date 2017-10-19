#!/bin/bash

set -e

BASEDIR=$(dirname $0)

# login to private docker registry
IMAGE=026043779925.dkr.ecr.us-west-2.amazonaws.com/tomcat

cd .. && jar -xvf VN_sample.war

eval $(aws ecr get-login --region us-west-2 --no-include-email)

# Build the app image:
docker build --force-rm=true -t $IMAGE:$VERSION .

# Push both images
docker push $IMAGE:$VERSION
