import sys

N, K = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        dp[i][j] = max(arr[i - 1][1] + dp[i - 1][j - arr[i - 1][0]], dp[i - 1][j]) if j >= arr[i - 1][0] else dp[i - 1][j]
print(dp[N][K])