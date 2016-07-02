.PHONY: all data/groupby.db data/load.db python_groupby python_load use_large_sample use_small_sample clean

all: data/groupby.db data/load.db python_groupby python_load

file := data/sample.$(n).csv

$(file):
	python gen_csv.py $(n) $@

test_sql: $(file)
	time test/test.sh $(file) $(command)

test_python: $(file)
	time python test/test.py $(file) $(command)

clean:
	rm -f data/*.csv
