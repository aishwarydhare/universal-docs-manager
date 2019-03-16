#!/bin/sh

outputFile="../tmp/my_output.txt"
# May need: `chmod +x get_object_mysql.sh`

if ../src/get_object_mysql.sh "127.0.0.1" "root" "root" "temp" "25" "${outputFile}"; then
  echo 'OK'
  cat "${outputFile}"
  rm "${outputFile}"
else
  echo "Failed ($?)"
fi

