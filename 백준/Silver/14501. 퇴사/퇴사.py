import sys

input = sys.stdin.readline

arr = []

for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
dp = [0 for i in range(len(arr) + 1)]

for i in range(len(arr)):
    for j in range(i + arr[i][0], len(arr) + 1):
        dp[j] = max(dp[j], dp[i] + arr[i][1])

print(dp[-1])