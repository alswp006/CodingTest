import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
move = [(0,1), (1,0)]


for x in range(n):
    for y in range(n):
        if dp[x][y] == 0 and arr[x][y] == 0:
            dp[x][y] = 1
        if dp[x][y] > 0:
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if nx >= n or ny >= n:
                    continue
                if(dp[x][y]) % 3 == arr[nx][ny]:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
                else:
                    if dp[nx][ny] < dp[x][y]:
                        dp[nx][ny] = dp[x][y]

print(dp[n-1][n-1])