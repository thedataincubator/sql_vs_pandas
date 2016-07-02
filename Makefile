.PHONY: data/test.db clean

data/sample.csv:
	python gen_csv.py 100 > $@

data/test.db:
	if [ -f $@ ] ; then rm $@; fi
	sqlite3 $@ < test.sql

clean:
	rm -f data/sample.csv
