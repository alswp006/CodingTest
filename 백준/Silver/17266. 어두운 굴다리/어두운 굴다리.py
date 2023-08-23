import sys

input=sys.stdin.readline

n=int(input())
m=int(input())
arr=[0 for _ in range(n+1)]
arr=list(map(int,input().split()))
count=0
answer=0
for i in arr:
    if count==0:
        temp=i
        answer=i
        count+=1
    else:
        if (i-temp)%2==0:a=(i-temp)//2
        else:a=(i-temp)//2+1
        answer=max(a,answer)
        temp=i
answer=max(answer,n-temp)
print(answer)