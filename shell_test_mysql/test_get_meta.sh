#!/bin/sh

outputFile="../tmp/my_output.txt"
# May need: `chmod +x head_object_mysql.sh`

if ../src/head_object_mysql.sh "127.0.0.1" "root" "root" "temp" "38" "${outputFile}"; then
  echo 'OK'
  cat ${outputFile}
  rm "${outputFile}"
else
  echo "Failed ($?)"
fi

