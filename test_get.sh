#!/bin/sh

export AWS_CONFIG_FILE='./.my-aws-config'

# May need: `chmod +x get_object_s3.sh`

if ./get_object_s3.sh 'myDirectoryName/myFileName.xml' 'repos-master-bucket' 'us-east-2' 'my_output.xml'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

