import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)
    arr[end].append(start)

for i in range(len(arr)):
    arr[i].sort()

dfs_visited = [False for i in range(n + 1)]
bfs_visited = [False for i in range(n + 1)]


def dfs(x):
    print(x, end=' ')
    dfs_visited[x] = True
    for i in arr[x]:
        if dfs_visited[i] == False:
            dfs(i)


def bfs(x):
    q = deque()
    q.append(x)
    bfs_visited[x] = True
    while q:
        temp = q.popleft()
        print(temp, end=' ')
        for i in arr[temp]:
            if bfs_visited[i] == False:
                bfs_visited[i] = True
                q.append(i)

dfs(v)
print()
bfs(v)