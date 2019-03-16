#!/bin/sh

inputFile="/Users/aishwarydhare/Work/python/universal-docs-manager/tmp/samplefile.txt"
# May need: `chmod +x upload_object_mysql.sh`

../src/upload_object_mysql.sh "127.0.0.1" "root" "root" "temp" "${inputFile}"
echo "stored with primary key id: $?"

