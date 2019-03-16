#!/bin/sh

export AWS_CONFIG_FILE='../.my-aws-config'

# May need: `chmod +x get_bucket_list_s3.sh`

if ../src/get_bucket_list_s3.sh 'my-test-name' 'ap-south-1' '../tmp/my_output.xml' ''; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

