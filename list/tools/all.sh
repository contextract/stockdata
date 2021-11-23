#!/bin/sh

DIR=$(dirname $0)
CMD=$(basename $0)

usage()
{
	echo "Usage: $CMD [Out Directory] [Old Directory]"
}

failed()
{
	echo $1
}

OUT=$1
OLD=$2
TMP=$(mktemp -d)

if [ $# -lt 2 ]
then
	usage
	exit 1
fi

if [ ! -e $OLD ]
then
	failed "Old directory does not exist"
fi

if [ -e $OUT ]
then
	if [ ! -d $OUT ]
	then
		failed "Output directory is not a directory"
	fi
else
	mkdir $OUT
fi

# KR
python3 $DIR/kr-download.py $TMP || failed "KR Download failed"

tail -n +2 $TMP/stock.csv > $TMP/items.csv
tail -n +2 $TMP/etf.csv >> $TMP/items.csv
tail -n +2 $TMP/etn.csv >> $TMP/items.csv

echo $TMP/items.csv

python3 $DIR/kr.py $TMP/items.csv $OLD/items.csv > $OUT/items.csv

# US
$DIR/us.sh $OUT

# reuter
python3 $DIR/reuter.py > $OUT/reuter.csv
