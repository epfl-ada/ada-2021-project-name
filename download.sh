#!/bin/bash

DATA_DIR=data

if [ ! -d "$DATA_DIR" ]
then
  mkdir $DATA_DIR
fi

for YEAR in {2020..2020}
do
    FILE=quotes-${YEAR}.json
    wget https://zenodo.org/record/4277311/files/${FILE}.bz2
    gunzip -k ${FILE}.bz2
    rm ${FILE}.bz2
    python scripts/preprocess.py --file=${FILE}
    rm ${FILE}
    mv quotes-${YEAR}-processed.json ${DATA_DIR}
done