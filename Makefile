.PHONY: all data/groupby.db data/load.db python_groupby python_load use_large_sample use_small_sample clean

all: data/groupby.db data/load.db python_groupby python_load

data/large.sample.csv:
	python gen_csv.py 1000000 $@

data/small.sample.csv:
	python gen_csv.py 100 $@

use_large_sample: data/large.sample.csv
	if [ -f data/sample.csv ] ; then rm data/sample.csv; fi
	cp data/large.sample.csv data/sample.csv

use_small_sample: data/small.sample.csv
	if [ -f data/sample.csv ] ; then rm data/sample.csv; fi
	cp data/small.sample.csv data/sample.csv

data/groupby.db:
	echo "SQL Groupby Test"
	if [ -f $@ ] ; then rm $@; fi
	time sqlite3 $@ < test/groupby.sql > /dev/null

data/load.db:
	echo "SQL Load Test"
	if [ -f $@ ] ; then rm $@; fi
	time sqlite3 $@ < test/load.sql > /dev/null

python_groupby:
	echo "Pandas Groupby Test"
	time python test/groupby.py > /dev/null

python_load:
	echo "Pandas Load Test"
	time python test/load.py > /dev/null

clean:
	rm -f data/sample.csv
