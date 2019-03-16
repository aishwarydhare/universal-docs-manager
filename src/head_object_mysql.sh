#!/bin/sh

mysqlHost="${1:-mysql host not provided}"
mysqlUser="${2:-mysql user not provided}"
mysqlPass="${3:-mysql password not provided}"
mysqlDb="${4:-mysql db not provided}"
row="${5:-row id (primarykey) not provided}"
outputFile="${6:-file to store output not provided}"

echo "Fetching meta-data from ${row} blob from MySQL" "->" "${outputFile}"

sql="SELECT created_at, modified_at, name, size, contentType, extras FROM uploads where id=${row}"
sqlOutput=$(mysql -N -h"${mysqlHost}" -u"${mysqlUser}" -p"${mysqlPass}" ${mysqlDb} -e "${sql}")

res=$(echo "${sqlOutput}" | tr '\t' ',')
#res=$(echo "${res}" | tr ' ' '')

set -f                      # avoid globbing (expansion of *).
array=(${res//,/ })

echo "CreatedAt:${array[0]} ${array[1]}" >> "${outputFile}"
echo "LastModified:${array[2]} ${array[3]}" >> "${outputFile}"
echo "Name:${array[4]}" >> "${outputFile}"
echo "Size:${array[5]}" >> "${outputFile}"
echo "ContentType:${array[6]}" >> "${outputFile}"
echo "Extras:${array[7]}" >> "${outputFile}"

exit 0
