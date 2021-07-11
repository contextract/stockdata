#!/bin/bash

DIR=$(dirname $0)
CMD=$(basename $0)

echo $DIR

usage()
{
	echo "Usage: $CMD [Out Directory]"
}

OUT=$1
TMP=$(mktemp -d)

if [ $# -lt 1 ]
then
	usage
	exit 1
fi

if [ ! -e $OUT ]
then
	mkdir $OUT
fi

wget ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt -O $TMP/nasdaq.csv
wget ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt -O $TMP/other.csv

head -n -1 $TMP/nasdaq.csv > $OUT/nasdaq.csv
head -n -1 $TMP/other.csv > $OUT/other.csv
