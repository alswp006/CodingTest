import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
visited=[0]*(n+1)
dfs(1)
print(sum(visited)-1)
