import sys

int(input())
arr=list(map(int,sys.stdin.readline().split()))
m = max(arr)
answer=0

for i in arr:
    if i==m:
        answer+=m
        m=0
        continue
    answer+=i/2
if answer-int(answer)==0:
    print(int(answer))
else:
    print(answer)