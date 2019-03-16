#!/bin/sh -u

targetFile="${1:-exmaple-my-file}"
outputFile="${2:-tmp-output-file}"

echo "Loading file meta" "<-" "${targetFile}"

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

get_abs_filename() {
  # $1 : relative filename
  echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

echo "LastModified:$(ls -l ${targetFile} | awk '{printf ("%s %s %s ",  $6,  $7, $8);}')" >> "${outputFile}"
echo "Name:$(basename ${targetFile})" >> "${outputFile}"
echo "Size:$(ls -i ${targetFile} | awk '{printf ("%s",  $1);}')" >> "${outputFile}"
echo "ContentType:$(file -b --mime-type ${targetFile})" >> "${outputFile}"
echo "Path:$(get_abs_filename "${targetFile}")" >> "${outputFile}"

exit 0
