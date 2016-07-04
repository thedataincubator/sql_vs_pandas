.PHONY: all test_sql test_python clean

file := data/sample.$(n).csv
bonus := data/bonus.$(n).csv

all: drive bonus

$(file):
	python gen/gen_csv.py $(n) $@

$(bonus): $(file)
	cat $< | python gen/bonus_csv.py > $@

drive: $(file)
	python driver/driver.py $(file) $(program)

sqlite_load:
	driver/sqlite_load.sh $(file)

clean:
	rm -f data/*.csv

deploy:
	git push vagrant master

pull-results:
	rsync -r vagrant:~/sql_vs_pandas/results/ results/
