from collections import deque
import sys

input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v,visited):
    visited[v]=True
    print(v,end=' ')
    graph[v].sort()
    for i in graph[v]:
        if visited[i]==False:
            dfs(i,visited)

def bfs(v,visited):
    q=deque([v])
    visited[v]=True
    while q:
        c=q.popleft()
        print(c,end=' ')
        graph[c].sort()
        for i in graph[c]:
            if visited[i]==False:
                q.append(i)
                visited[i]=True

visited=[False] *(n+1)
dfs(v,visited)
print()
visited=[False] *(n+1)
bfs(v,visited)