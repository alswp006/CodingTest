import sys

input = sys.stdin.readline
dp = [1 + i//2 for i in range(10001)]

for i in range(3, 10001):
    dp[i] += dp[i - 3]

for i in range(int(input())):
    print(dp[int(input())])