import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = sorted([int(input()) for _ in range(n)], reverse=True)
dp = [10 ** 5] * (k + 1)

for i in coin:
    if i < k + 1:
        dp[i] = 1
    for j in range(i, len(dp)):
        dp[j] = min(dp[j-i] + 1, dp[j])

print(dp[-1] if dp[-1] != 10**5 else -1)