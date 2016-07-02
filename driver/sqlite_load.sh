TEST_DB='data/test.db'
FILE=$1

# delte $TEST_DB if it exists
if [ -f $TEST_DB ] ;
then
  rm $TEST_DB;
fi

LOAD="CREATE TABLE test (name varchar(255), dept char(1), birth int, salary double);\n"\
".separator \",\"\n"\
".import ${FILE} test\n"

# load data
echo $LOAD | sqlite3 $TEST_DB > /dev/null
