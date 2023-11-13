from collections import deque

n,m = map(int,input().split())

arr=deque(i+1 for i in range(n))

print("<" ,end='')
while arr:
    arr.rotate(-(m-1))
    print(arr.popleft(), end='')
    if len(arr)==0:
        print(">")
        break
    print(", ",end='')