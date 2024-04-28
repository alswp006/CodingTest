import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for i in range(n)]
if n == 1:
    dp = [arr[0]]
elif n == 2:
    dp = [arr[0] + arr[1]]
else:
    dp = [arr[0], arr[0] + arr[1], max(arr[2] + arr[1], arr[2] + arr[0], arr[1] + arr[0])] + [0] * (n - 3)

for i in range(3, n):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i - 3], dp[i-1])
print(dp[-1])
