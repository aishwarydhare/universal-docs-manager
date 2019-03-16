#!/bin/sh -u

targetFile="${1:-exmaple-my-file}"

echo "Deleting file meta" "->" "${targetFile}"

if [ -d "${targetFile}" ] ; then
    echo "targetFile is a directory";
    exit 1
else
    if [ -f "${targetFile}" ]; then
        r=1
    else
        echo "${targetFile} is not valid a file";
        exit 1
    fi
fi

rm "${targetFile}"

exit 0
