#!/bin/sh -u

blob="${1:-hello world!}"
targetFile="${2:-example-new-name}"

echo "Storing file" "->" "${targetFile}"
echo "${blob}" > "${targetFile}"

exit 0
