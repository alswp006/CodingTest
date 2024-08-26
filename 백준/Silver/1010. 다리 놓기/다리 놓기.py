import math, sys

for _ in range(int(input())):
    n,m=map(int,sys.stdin.readline().split())
    print(math.comb(m, n))