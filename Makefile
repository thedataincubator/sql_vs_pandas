.PHONY: all test_sql test_python clean

all: drive

file := data/sample.$(n).csv

$(file):
	python gen_csv.py $(n) $@

drive: $(file)
	python driver/driver.py $(file) $(command)

sqlite_load:
	driver/sqlite_load.sh $(file)

clean:
	rm -f data/*.csv
