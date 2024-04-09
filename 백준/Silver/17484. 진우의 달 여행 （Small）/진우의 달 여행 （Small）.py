import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dp = [[[0 for _ in range(3)] for _ in range(m)] for _ in range(n)]
arr = [list(map(int, input().split())) for i in range(n)]

for j in range(m):
    if j != 0 :
        dp[1][j][0] = arr[1][j] + arr[0][j - 1]
    dp[1][j][1] = arr[1][j] + arr[0][j]
    if j != m - 1:
        dp[1][j][2] = arr[1][j] + arr[0][j + 1]

for i in range(2, n):
    for j in range(m):
        if j == 0:
            dp[i][j][1] = arr[i][j] + dp[i - 1][j][2]
            dp[i][j][2] = arr[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])
        elif j == m - 1:
            dp[i][j][0] = arr[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            dp[i][j][1] = arr[i][j] + dp[i - 1][j][0]
        else:
            dp[i][j][0] = arr[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
            dp[i][j][1] = arr[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])
            dp[i][j][2] = arr[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

answer = dp[-1][0][1]
for i in dp[-1]:
    for j in i:
        if j == 0:
            continue
        answer = min(answer, j)
print(answer)