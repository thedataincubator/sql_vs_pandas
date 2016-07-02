.PHONY: all test_sql test_python clean

all: driver

file := data/sample.$(n).csv

$(file):
	python gen_csv.py $(n) $@

drive: $(file)
	time python driver/driver.py $(file) $(command)

sqlite_load:
	time driver/sqlite_load.sh $(file)

clean:
	rm -f data/*.csv
