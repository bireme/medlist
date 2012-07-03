#!/bin/bash

CUR_TIME=`date "+%Y/%m/%d %H:%M:%S"`

MEDLIST_URL="http://medlist.homolog.bvsalud.org"
TEMP_FILE="/tmp/index_medlist.txt"
LOG_FILE="/tmp/index_medlist.log"

echo "[$CUR_TIME] getting service which index all content.."
wget -o $LOG_FILE -O $TEMP_FILE $MEDLIST_URL/api/index

echo [$CUR_TIME] `cat $TEMP_FILE`

echo [$CUR_TIME] removing temporary files..
rm $TEMP_FILE

echo "[$CUR_TIME] done!"

