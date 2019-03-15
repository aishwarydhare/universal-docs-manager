#!/bin/sh

export AWS_CONFIG_FILE='./.my-aws-config'

# May need: `chmod +x delete_object_s3.sh`

if ./delete_object_s3.sh 'myTest.xml' 'repos-master-bucket' 'us-east-2'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

