DIR=$1

mkdir -p $DIR

for n in 1000 10000 100000 1000000 10000000
do
  echo $n >> $DIR/sqlite_load.txt
  { time make -s sqlite_load n=$n; } 2>> $DIR/sqlite_load.txt

  for program in pandas sqlite memory-sqlite
  do
    for i in {1..10}
    do
      make -s drive n=$n program=$program >> $DIR/driver.json
    done
  done
done
