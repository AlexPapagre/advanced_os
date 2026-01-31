#!/usr/bin/env bash

set -e

docker run -it \
    -p 8080:8080 \
    -p 8081:8081 \
    -p 6066:6066 \
    -p 7077:7077 \
    -v ./data:/opt/data \
    -v ./outputs:/opt/outputs \
    spark-app
