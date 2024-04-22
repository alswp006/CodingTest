import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
map_info = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
distance = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q=deque()

for i in range(n):
    for j in range(m):
        if map_info[i][j] == 0:
            answer[i][j] = 0
        elif map_info[i][j] == 2:
            q.append([i, j, 0])
            answer[i][j] = 0


while q:
    x, y, num = q.popleft()
    for i in range(4):
        dx, dy = x + distance[i][0], y + distance[i][1]
        if dx < 0 or dy < 0 or dx >= n or dy >= m:
            continue
        if answer[dx][dy] != -1:
            continue
        if map_info[dx][dy] != 1:
            answer[dx][dy] = 0
            continue
        answer[dx][dy] = num + 1
        q.append([dx, dy, num + 1])


for i in answer:
    print(*i)