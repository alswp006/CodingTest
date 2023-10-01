import sys

input = sys.stdin.readline

n=int(input())
m=int(input())
arr=list(map(int,input().split()))
arr.sort()
i=0
j=len(arr)-1
answer=0

if n==1:
    print(0)
    exit()
while i<j:
    if arr[i]+arr[j]==m:
        answer+=1
        i+=1
        j-=1
    elif arr[i]+arr[j]<m:
        i+=1
    else:
        j-=1
print(answer)