#!/bin/sh

inputFile="/Users/aishwarydhare/Work/python/universal-docs-manager/tmp/samplefile.txt"
outputFile="/Users/aishwarydhare/Work/python/universal-docs-manager/tmp/my_output.txt"

# May need: `chmod +x upload_object_local.sh`

if ../src/upload_object_local.sh "${inputFile}" "${outputFile}"; then
  echo 'OK'
else
  echo "Failed ($?)"
fi

