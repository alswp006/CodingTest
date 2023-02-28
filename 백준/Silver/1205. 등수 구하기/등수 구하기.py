import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())

if n>0: arr=list(map(int,input().split()))
else:arr=[]
if len(arr)==0:
    print(1)
else:
    if arr[-1]>=m:
        if len(arr)>=k:
            print(-1)
        else:
            arr.append(m)
            arr.sort(reverse=True)
            print(arr.index(m)+1)
    else:
        arr.append(m)
        arr.sort(reverse=True)
        print(arr.index(m)+1)