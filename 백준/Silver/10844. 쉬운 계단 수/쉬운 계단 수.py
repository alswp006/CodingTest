n = int(input())

dp = [[0] * 10 for i in range(n + 1)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0 and i != 2:
            dp[i][j + 1] += dp[i-1][j]
        elif j == 9:
            dp[i][j - 1] += dp[i-1][j]
        else:
            dp[i][j - 1] += dp[i-1][j]
            dp[i][j + 1] += dp[i-1][j]

print(sum(dp[-1])%1000000000)