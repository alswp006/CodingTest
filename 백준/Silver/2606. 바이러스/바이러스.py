import sys

input = sys.stdin.readline


def dfs(node, visited=[]):
    visited.append(node)

    for i in arr[node]:
        if not i in visited:
            visited = dfs(i, visited)
    return visited


arr = [[] for i in range(int(input()) + 1)]
count = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

print(len(dfs(1, visited=[])) - 1)