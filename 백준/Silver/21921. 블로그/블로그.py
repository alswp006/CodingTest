from collections import deque

n,m=map(int,input().split())
arr=list(map(int,input().split()))
num=1
answer=0
for i in range(m):
    answer+=arr[i]
temp=answer
for i in range(m,len(arr)):
    temp=temp-arr[i-m]+arr[i]
    if temp<=answer:
        if temp==answer:num+=1
    else:
        answer=temp
        num=1
if answer==0:
    print('SAD')
else:
    print(answer)
    print(num)