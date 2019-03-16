#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'

# May need: `chmod +x get_object_s3.sh`

if ../src/get_object_s3.sh 'myDirectoryName/myTwoFileName.xml' 'sample-bucket' 'us-east-2' '../tmp/my_output.xml'; then
  echo 'OK'
  cat '../tmp/my_output.xml'
  rm '../tmp/my_output.xml'
else
  echo "Failed ($?)"
fi

