import sys
input = sys.stdin.readline

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0

def dfs(x, y, idx, total):
    if idx == 3:
        return total
    max_val = 0
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if is_valid(nx, ny):
            visit[nx][ny] = 1
            if idx == 1:
                max_val = max(max_val, dfs(x, y, idx + 1, total + arr[nx][ny]))
            max_val = max(max_val, dfs(nx, ny, idx + 1, total + arr[nx][ny]))
            visit[nx][ny] = 0
    return max_val

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_val = 0

for x in range(N):
    for y in range(M):
        visit[x][y] = 1
        max_val = max(max_val, dfs(x, y, 0, arr[x][y]))
        visit[x][y] = 0

print(max_val)