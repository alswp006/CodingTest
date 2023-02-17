from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
x,y=map(int,input().split())
m=int(input())
arr=[[] for _ in range(n+1)]
distance=[-1]*(n+1)
visited=[False]*(n+1)
distance[x]=0
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
q=deque([x])
while q:
    now=q.popleft()
    for i in arr[now]:
        if distance[i]==-1:
            distance[i]=distance[now]+1
            q.append(i)
print(distance[y])