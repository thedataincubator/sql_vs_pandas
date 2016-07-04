.PHONY: all clean sqlite-load drive sqlite-limit

file := data/sample.$(n).csv
bonus := data/bonus.$(n).csv

all: drive

$(file):
	python gen/gen_csv.py $(n) $@

$(bonus): $(file)
	cat $< | python gen/bonus_csv.py > $@

drive: $(file) $(bonus)
	python driver/driver.py $(n) $(file) $(bonus) $(program)

sqlite-load:
	driver/sqlite_load.sh $(file) $(bonus)

sqlite-limit:
	driver/sqlite_load.sh $(file) $(bonus) full

clean:
	rm -f data/*.csv

deploy:
	git push vagrant master

pull-results:
	rsync -r vagrant:~/sql_vs_pandas/results/ results/
