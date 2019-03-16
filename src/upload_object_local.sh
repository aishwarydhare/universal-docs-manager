#!/bin/sh -u

sourceFile="${1:-hello world!}"
targetFile="${2:-example-new-name}"

echo "Storing file" "->" "${targetFile}"
cat "${sourceFile}" > "${targetFile}"

exit 0
