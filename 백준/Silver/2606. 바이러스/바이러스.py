from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]
answer=0
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(graph,v,visited):
    global answer
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            answer+=1
            dfs(graph,i,visited)
visited=[False]*(n+1)
dfs(graph,1,visited)
print(answer)