.PHONY: data/test.db use_large_sample use_small_sample clean

all: data/test.db python_test

data/large.sample.csv:
	python gen_csv.py 1000000 $@

data/small.sample.csv:
	python gen_csv.py 100 $@

use_large_sample: data/large.sample.csv
	if [ -f data/sample.csv ] ; then rm data/sample.csv; fi
	ln -s data/large.sample.csv data/sample.csv

use_small_sample: data/small.sample.csv
	if [ -f data/sample.csv ] ; then rm data/sample.csv; fi
	ln -s data/small.sample.csv data/sample.csv

data/test.db:
	if [ -f $@ ] ; then rm $@; fi
	time sqlite3 $@ < test.sql > /dev/null

python_test:
	time python test.py > /dev/null

clean:
	rm -f data/sample.csv
