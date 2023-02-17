from collections import deque
import sys

input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        c=q.popleft()
        print(c,end=' ')
        for i in sorted(graph[c]):
            if not visited[i]:
                q.append(i)
                visited[i]=True

visited=[False] *(n+1)
dfs(v)
print()
visited=[False] *(n+1)
bfs(v)