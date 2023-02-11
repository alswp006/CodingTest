import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
if sum(arr)<m:
    print(max(arr))
else:
    while arr:
        x=m//n
        for i in arr:
            if i<x:
                m-=i
                n-=1
                arr.remove(i)
                break
        else:
            break    
    print(m//n)