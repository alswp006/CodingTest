import sys

input=sys.stdin.readline
n=int(input())
s=set()
num=[i for i in range(1,21)]
for i in range(n):
    arr=list(map(str,input().split()))
    if len(arr)==1:
        if arr[0]=="all":
            s.update(num)
        elif arr[0]=="empty":
            s.clear()
        continue
        
    arr[1]=int(arr[1])
    if arr[0]=="add":
        s.add(arr[1])
    elif arr[0]=="remove":
        if arr[1] in s:s.discard(arr[1])
    elif arr[0]=="check":
        if arr[1] in s:print(1)
        else:print(0)
    elif arr[0]=="toggle":
        if arr[1] in s:s.remove(arr[1])
        else: s.add(arr[1])