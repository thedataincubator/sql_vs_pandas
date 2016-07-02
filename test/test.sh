TEST_DB='data/test.db'
FILE=$1
COMMAND=$2

# delte $TEST_DB if it exists
if [ -f $TEST_DB ] ;
then
  rm $TEST_DB;
fi

LOAD="CREATE TABLE test (name varchar(255), dept char(1), birth int, salary double);\n"\
".separator \",\"\n"\
".import ${FILE} test\n"

GROUPBY='SELECT avg(birth), sum(salary) FROM test GROUP BY dept;'

if [ "$COMMAND" = "load" ]; then
  QUERY=$LOAD;
elif [ "$COMMAND" = "groupby" ]; then
  QUERY=$LOAD$GROUPBY;
fi

# load data
echo $QUERY | sqlite3 $TEST_DB > /dev/null
