make all n=1000 command=load
make all n=10000 command=load
make all n=100000 command=load
make all n=1000000 command=load

for n in (1000 10000 100000 1000000)
do
  for command in (load groupby)
  do
    make all n=$(n) command=$(command)
  done
done
