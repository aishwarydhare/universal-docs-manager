#!/bin/sh

inputFile="../tmp/samplefile.txt"
outputFile="../tmp/tmp.txt"
# May need: `chmod +x upload_object_mysql.sh`

if ../src/upload_object_mysql.sh "127.0.0.1" "root" "root" "temp" "${inputFile}" "${outputFile}"; then
  echo "stored with primary key id: $(cat "${outputFile}")"
  rm "${outputFile}"
else
  echo "Failed ($?)"
fi
