#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'

# May need: `chmod +x get_object_s3.sh`

if ../src/head_object_s3.sh 'myDirectoryName/myTwoFileName.xml' 'repos-master-bucket' 'us-east-2' '../tmp/my_head_output.txt'; then
  echo 'OK'
  cat '../tmp/my_head_output.txt'
  rm '../tmp/my_head_output.txt'
else
  echo "Failed ($?)"
fi
