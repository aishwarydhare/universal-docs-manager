#!/bin/sh

# May need: `chmod +x delete_object_local.sh`

if ../src/delete_object_local.sh '../tmp/mfile.txt'; then
  echo 'OK'
else
  echo "Failed ($?)"
fi
