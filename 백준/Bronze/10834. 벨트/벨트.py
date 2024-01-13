import sys

input = sys.stdin.readline

answer = 1
rotate = 0

for _ in range(int(input())):
    n,m,k = map(int,input().split())
    answer/=n
    answer*=m
    if k == 1:
        rotate+=1
print(rotate%2, int(answer))