#!/bin/sh

# May need: `chmod +x head_object_local.sh`

if ../src/head_object_local.sh '../src/head_object_local.sh' '../tmp/my_output.txt'; then
  echo 'OK'
  cat '../tmp/my_output.txt'
  rm '../tmp/my_output.txt'
else
  echo "Failed ($?)"
fi
