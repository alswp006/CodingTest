import sys
from collections import deque
input=sys.stdin.readline
top,start,end,up,down=map(int,input().split())
d=[0 for _ in range(top+2)]
q=deque()
q.append(start)
while q:
    x=q.popleft()
    if x==end:
        print(d[end])
        break
    dx=[x+up,x-down]
    for i in dx:
        if i==x:continue
        if 0<i<top+1 and not d[i]:
            d[i]=d[x]+1
            q.append(i)
else: print("use the stairs") 