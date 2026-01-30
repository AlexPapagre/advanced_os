#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <SPARK_MASTER_HOSTNAME>"
    exit 1
fi

HOSTNAME=$1

curl -X POST http://"$HOSTNAME":6066/v1/submissions/create \
    -H "Content-Type:application/json;charset=UTF-8" \
    -d "{
    \"action\": \"CreateSubmissionRequest\",
    \"appResource\": \"file:///app/main.py\",
    \"clientSparkVersion\": \"3.4.2\",
    \"mainClass\": \"org.apache.spark.deploy.PythonRunner\",
    \"appArgs\": [\"/app/main.py\", \"\", \"\"],
    \"environmentVariables\": {},
    \"sparkProperties\": {
      \"spark.app.name\": \"MainPy\",
      \"spark.master\": \"spark://$HOSTNAME:7077\",
      \"spark.submit.deployMode\": \"cluster\",
      \"spark.driver.supervise\": \"false\"
    }
  }"
