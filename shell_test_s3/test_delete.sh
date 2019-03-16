#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'

# May need: `chmod +x delete_object_s3.sh`

if ../src/delete_object_s3.sh 'myDirectoryName/myTwoFileName.xml' 'sample-bucket' 'us-east-2'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

