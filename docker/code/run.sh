#!/bin/sh
echo Copying data
aws s3 cp s3://xxx-input-bucket/input/ /input/ --recursive

python3 run.py

echo saving model
aws s3 cp ./model.tar.gz s3://xxx-output-bucket/output/