ulimit -Sv 1000000
ulimit -Sv
make all n=10000000 program=pandas

make sqlite-limit n=10000000
