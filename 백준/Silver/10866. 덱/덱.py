import sys
from collections import deque

input=sys.stdin.readline
q=deque()
for _ in range(int(input())):
    arr=list(map(str,input().split()))
    if len(arr)==1:
        if arr[0]=='front':
            if len(q)==0:print(-1)
            else: print(q[0])
        elif arr[0]=='back':
            if len(q)==0:print(-1)
            else: print(q[-1])
        elif arr[0]=='size':
            print(len(q))
        elif arr[0]=='empty':
            if len(q)==0:print(1)
            else: print(0)
        elif arr[0]=='pop_front':
            if len(q)==0:print(-1)
            else: print(q.popleft())
        elif arr[0]=='pop_back':
            if len(q)==0:print(-1)
            else: print(q.pop())
    else:
        if arr[0]=='push_front':
            q.appendleft(int(arr[1]))
        if arr[0]=='push_back':
            q.append(int(arr[1]))