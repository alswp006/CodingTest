import math

for _ in range(int(input())):
    n,m=map(int,input().split())
    print(math.comb(max(n,m), min(n,m)))