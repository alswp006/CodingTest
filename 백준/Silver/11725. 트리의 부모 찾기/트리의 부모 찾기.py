import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(x):
    visited[x] = True

    for i in tree[x]:
        if visited[i]:
            continue
        parent_node[i] = x
        dfs(i)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent_node = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for i in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

dfs(1)

for i in parent_node[2:]:
    print(i)


