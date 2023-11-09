import sys

input = sys.stdin.readline
while True:
    n,m = map(int,input().split())
    if n==0 and m==0:break
    d1 = []
    for i in range(n+m):
        d1.append(int(input()))
    print(n+m-len(set(d1)))