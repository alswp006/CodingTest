import sys
input=sys.stdin.readline

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return 1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

n=int(input())
number=list(map(int,input().split()))
m=int(input())
number2=list(map(int,input().split()))
number.sort()
for i in number2:
    sys.stdout.write(str(binary_search(number,i,0,n-1))+'\n')