#!/usr/bin/env bash

set -e

docker run --rm \
    -v ./data:/opt/data \
    -v ./outputs:/opt/outputs \
    pandas-app
