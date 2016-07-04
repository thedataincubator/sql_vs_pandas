.PHONY: all clean sqlite_load drive

file := data/sample.$(n).csv
bonus := data/bonus.$(n).csv

all: drive

$(file):
	python gen/gen_csv.py $(n) $@

$(bonus): $(file)
	cat $< | python gen/bonus_csv.py > $@

drive: $(file) $(bonus)
	python driver/driver.py $(n) $(file) $(bonus) $(program)

sqlite_load:
	driver/sqlite_load.sh $(file) $(bonus)

clean:
	rm -f data/*.csv

deploy:
	git push vagrant master

pull-results:
	rsync -r vagrant:~/sql_vs_pandas/results/ results/
