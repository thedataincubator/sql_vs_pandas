.PHONY: all test_sql test_python clean

all: test_sql test_python

file := data/sample.$(n).csv

$(file):
	python gen_csv.py $(n) $@

test_sql: $(file)
	time test/test.sh $(file) $(command)

test_python: $(file)
	time python test/test.py $(file) $(command)

clean:
	rm -f data/*.csv
