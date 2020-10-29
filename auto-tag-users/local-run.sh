#!/bin/bash

docker build -t aws-utilities:0.0.1 .
directory=`pwd`
docker run --volume $directory:/app aws-utilities:0.0.1
