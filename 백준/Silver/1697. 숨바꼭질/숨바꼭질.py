from collections import deque

n,m=map(int,input().split())
d=[0 for _ in range(100001)]

q=deque()
q.append(n)
while q:
    x=q.popleft()
    if x==m:break
    dx=[x-1,x+1,x*2]
    for i in dx:
        if 0<=i<100001 and not d[i]:
            d[i]=d[x]+1
            q.append(i)
print(d[m])