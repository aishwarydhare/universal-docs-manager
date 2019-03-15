#!/bin/sh

export AWS_CONFIG_FILE='./.my-aws-config'

echo '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' > samplefile.xml
echo '<tester>' >> samplefile.xml
echo '</tester>' >> samplefile.xml

# May need: `chmod +x upload_s3.sh`

if ./upload_object_s3.sh 'samplefile.xml' 'repos-master-bucket' 'us-east-2' 'STANDARD' 'myDirectoryName/myTwoFileName.xml'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

