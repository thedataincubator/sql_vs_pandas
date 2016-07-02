DIR=$1

mkdir -p $DIR

for n in 1000 10000 100000 1000000 10000000
do
  for command in pandas sqlite
  do
    for i in {1..10}
    do
      make all n=$n command=$command > $DIR/$(date +%s%N).json
    done
  done
done
