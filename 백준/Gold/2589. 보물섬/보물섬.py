import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
d = [(0,1), (0,-1), (1,0), (-1,0)]
answer = []
for i in range(n):
    arr.append(list(input().rstrip()))
visited = [[-1 for i in range(m)] for j in range(n)]


def init():
    for i in range(n):
        for j in range(m):
            visited[i][j] = -1
def bfs(x,y):
    q=deque()
    q.append((x, y))
    while q:
        x1, y1 = q.popleft()
        for i in range(4):
            nx = x1 + d[i][0]
            ny = y1 + d[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            if arr[nx][ny] == "W":
                continue
            if visited[nx][ny] != -1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = visited[x1][y1] + 1
    max_value = 0
    for i in range(n):
        max_value = max(max_value, max(visited[i]))

    return max_value


for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            visited[i][j] = 0
            answer.append(bfs(i,j))
            init()

print(max(answer))
