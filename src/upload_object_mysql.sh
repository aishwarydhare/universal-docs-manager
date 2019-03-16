#!/bin/sh

mysqlHost="${1:-mysql host not provided}"
mysqlUser="${2:-mysql user not provided}"
mysqlPass="${3:-mysql password not provided}"
mysqlDb="${4:-mysql db not provided}"
targetFile="${5:-file to store not provided}"
outputFile="${6}" # optional
extras="${7}"

if [ -f "${targetFile}" ]; then
  payloadDump=$(xxd ${targetFile})
else
  echo "File not found: '${targetFile}'"
  exit 1
fi

echo "Storing ${targetFile} blob" "->" "MySQL"

mysql -h"${mysqlHost}" -u"${mysqlUser}" -p"${mysqlPass}" $mysqlDb -e "
CREATE TABLE IF NOT EXISTS uploads
(
  id          int auto_increment
    primary key,
  name        text                               null,
  data        mediumblob                         null,
  created_at  datetime default CURRENT_TIMESTAMP null,
  modified_at datetime default CURRENT_TIMESTAMP null,
  size        mediumtext                         null,
  contentType text                               null,
  extras      text                               null
);
"

fileContentType=$(file -b --mime-type ${targetFile})
fileSize=$(ls -i ${targetFile} | awk '{printf ("%s",  $1);}')
name=$(basename ${targetFile})
sql="INSERT INTO uploads (created_at, modified_at, name, data, size, contentType, extras) VALUES (NOW(), NOW(), '${name}','${payloadDump}', '${fileSize}','${fileContentType}', '${extras}');"
mysql -h"${mysqlHost}" -u"${mysqlUser}" -p"${mysqlPass}" ${mysqlDb} -e "${sql}"

sql="SELECT id FROM uploads ORDER BY id DESC LIMIT 1"
latestId=$(mysql -N -h"${mysqlHost}" -u"${mysqlUser}" -p"${mysqlPass}" ${mysqlDb} -e "${sql}")

echo "${latestId}" > "${outputFile}"

exit 0
