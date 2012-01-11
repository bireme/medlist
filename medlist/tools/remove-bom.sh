#!/bin/bash

CURRENT=`pwd`

FILES=csv_dados/especial

cd ${FILES}



for f in *.*
do
  echo "Processing $f file..."
  
  tail --bytes=+4 ${f} > new/${f}
  
done

cd ${CURRENT}