import sys

input=sys.stdin.readline

def b_s(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return "1"
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return "0"
n=int(input())
num=list(map(int,input().split()))
m=int(input())
num2=list(map(int,input().split()))
num.sort()
for i in num2:
    sys.stdout.write(b_s(num,i,0,len(num)-1)+' ')