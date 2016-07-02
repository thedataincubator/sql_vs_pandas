for n in 1000 10000 100000 1000000 10000000
do
  for command in load groupby
  do
    make all n=$n command=$command
  done
done
