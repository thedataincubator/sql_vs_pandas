CREATE TABLE test (name varchar(255), dept char(1), birth int, salary double);

.separator ","
.import data/sample.csv test
