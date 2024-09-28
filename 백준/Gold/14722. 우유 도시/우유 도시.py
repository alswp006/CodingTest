import sys

n = int(input())
dp = [0] * (n + 1)
for step in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n + 1):
        cur = temp[i - 1]
        dp[i] = max(dp[i], dp[i - 1])
        dp[i] += dp[i] % 3 == cur
print(dp[n])