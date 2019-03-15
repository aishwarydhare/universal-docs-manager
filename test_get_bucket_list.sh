#!/bin/sh

export AWS_CONFIG_FILE='./.my-aws-config'

# May need: `chmod +x get_bucket_list_s3.sh`

if ./get_bucket_list_s3.sh 'repos-master-bucket' 'us-east-2' 'my_output.xml' 'myDirectoryName'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

