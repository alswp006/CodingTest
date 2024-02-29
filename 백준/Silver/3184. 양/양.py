import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(input().rstrip()) for i in range(n)]
d = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [[False for i in range(m)] for j in range(n)]
answer = [0,0]

def bfs(xx, yy):
    q = deque()
    q.append((xx, yy))
    v = 0
    o = 0
    while q:
        x, y = q.popleft()
        if arr[x][y] == "v":
            v += 1
        elif arr[x][y] == "o":
            o += 1
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == "#":
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny))

    return ["v", v] if v >= o else ["o", o]

for i in range(n):
    for j in range(m):
        if (arr[i][j] == "v" or arr[i][j] == "o") and visited[i][j] == False:
            visited[i][j] = True
            temp = bfs(i,j)
            if temp[0] == "v":
                answer[1] += temp[1]
            else:
                answer[0] += temp[1]

print(answer[0], answer[1])