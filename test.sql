create table test (name varchar(255), dept char(1), birth int, salary double);

.separator ","
.import data/sample.csv test

.output stdout
.echo off

SELECT COUNT(name) FROM test;
