DIR=$1

mkdir -p $DIR

for n in 1000 10000 100000 1000000 10000000
do
  for program in pandas sqlite memory-sqlite
  do
    for i in {1..10}
    do
      make -s all n=$n program=$program > $DIR/$(date +%s%N).json
    done
  done
done
