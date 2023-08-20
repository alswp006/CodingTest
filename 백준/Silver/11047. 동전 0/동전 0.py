from collections import deque

n,k = map(int,input().split())
arr=deque()
answer=0
for i in range(n):
    arr.appendleft(int(input()))
for i in arr:
    answer+=k//i
    k%=i
print(answer)