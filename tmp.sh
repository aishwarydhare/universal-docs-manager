#!/usr/bin/env bash
str="2019-03-16 19:13:20,2019-03-16 19:13:20,"
set -f                      # avoid globbing (expansion of *).
array=(${str//,/ })
for i in "${!array[@]}"
do
    echo "$i=>${array[i]}"
done