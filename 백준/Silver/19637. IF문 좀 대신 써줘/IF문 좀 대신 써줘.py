import sys
from bisect import bisect_left

input = sys.stdin.readline

n,m = map(int,input().split())

name = []
num = []

for i in range(n):
    a,b = map(str, input().split())
    if len(num) != 0 and num[-1] == int(b):
        continue
    name.append(a)
    num.append(int(b))

for i in range(m):
    power = int(input())
    print(name[bisect_left(num, power)])