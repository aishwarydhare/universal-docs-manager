#!/bin/sh

inputFile="../tmp/samplefile.txt"
outputFile="../tmp/my_output.txt"

# May need: `chmod +x upload_object_local.sh`

if ../src/upload_object_local.sh "${inputFile}" "${outputFile}"; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

