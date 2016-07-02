.PHONY: data/test.db clean

all: data/test.db python_test

data/sample.csv:
	python gen_csv.py 1000000 $@

data/test.db: data/sample.csv
	if [ -f $@ ] ; then rm $@; fi
	time sqlite3 $@ < test.sql > /dev/null

python_test: data/sample.csv
	time python test.py > /dev/null

clean:
	rm -f data/sample.csv
