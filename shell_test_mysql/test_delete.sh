#!/bin/sh

# May need: `chmod +x delete_object_mysql.sh`

if ../src/delete_object_mysql.sh "127.0.0.1" "root" "root" "temp" "25"; then
  echo 'OK'
else
  echo "Failed ($?)"
fi
