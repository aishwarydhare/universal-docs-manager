#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'

# May need: `chmod +x delete_bucket_s3.sh`

if ../src/delete_bucket_s3.sh 'sample-bucket' 'us-east-2'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

