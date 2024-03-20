n = int(input())
arr = list(map(int,input().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
print(max(dp))