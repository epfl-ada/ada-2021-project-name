#!/bin/bash

DATA_DIR=data

if [ ! -d "$DATA_DIR" ]
then
  mkdir $DATA_DIR
fi

for YEAR in {2008..2020}
do
    FILE=quotes-${YEAR}.json
    wget https://zenodo.org/record/4277311/files/${FILE}.bz2
    bzip2 -d ${FILE}.bz2
    python scripts/preprocess.py --file=${FILE}
    rm ${FILE}
    PROCESSED=quotes-${YEAR}-processed.json
    python scripts/merge.py --file=${PROCESSED}
    mv ${PROCESSED} ${DATA_DIR}
    MERGED=quotes-${YEAR}-merged.json
    mv ${MERGED} ${DATA_DIR}
done

cat $(echo ${DATA_DIR}/*-merged.json) > $DATA_DIR/union.json
python scripts/build_vocab.py --file=$DATA_DIR/union.json