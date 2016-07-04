TEST_DB='data/test.db'
EMPLOYEE_FILE=$1
BONUS_FILE=$2

# delte $TEST_DB if it exists
if [ -f $TEST_DB ] ;
then
  rm $TEST_DB;
fi

LOAD="CREATE TABLE employee (name varchar(255), dept char(1), birth int, salary double);\n"\
".separator \",\"\n"\
".import ${EMPLOYEE_FILE} employee\n"\
"\n"\
"CREATE TABLE bonus (name varchar(255), bonus double);\n"\
".separator \",\"\n"\
".import ${BONUS_FILE} bonus\n"

# load data
echo -e $LOAD | sqlite3 $TEST_DB > /dev/null
