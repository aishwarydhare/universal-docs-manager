#!/bin/sh
mysqlHost="${1:-mysql host not provided}"
mysqlUser="${2:-mysql user not provided}"
mysqlPass="${3:-mysql password not provided}"
mysqlDb="${4:-mysql db not provided}"
row="${5:-row id (primarykey) not provided}"

echo "Deleting ${row} blob " "->" "MySQL"

sql="DELETE FROM uploads where id=${row}"
blob=$(mysql -N -h"${mysqlHost}" -u"${mysqlUser}" -p"${mysqlPass}" ${mysqlDb} -e "${sql}")

exit 0
