import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    li=[0]
    for i in list(str(input())):
        if i=='R':
            li.append(0)
        elif i=='D':
            li[-1]+=1
    n=int(input())
    arr=input()
    if n==0 and sum(li)==0:
        print("[]")
        continue
    if sum(li)>n:
        print("error")
        continue
    arr=deque(map(int,arr[1:-2].split(",")))
    for i in range(len(li)):
        if i%2==0:
            for j in range(li[i]):arr.popleft()
        else:
            for j in range(li[i]):arr.pop()
    if len(li)%2!=0:
        print(str(list(arr)).replace(' ',''))
    else: 
        print(str(list(reversed(arr))).replace(' ',''))