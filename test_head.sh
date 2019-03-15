#!/bin/sh

export AWS_CONFIG_FILE='./.my-aws-config'

# May need: `chmod +x get_object_s3.sh`

if ./head_object_s3.sh 'myDirectoryName/myFileName.xml' 'repos-master-bucket' 'us-east-2' 'my_head_output.txt'; then
  echo 'OK'
  rm 'my_head_output.txt'
else
  echo "Failed ($?)"
fi

