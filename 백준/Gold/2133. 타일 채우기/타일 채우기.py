n = int(input())

if n % 2 != 0:
    print(0)
    exit()

dp = [0, 0, 3] + [0] * (n - 2)
temp = dp[2]

for i in range(4, n+1, 2):
    dp[i] = (dp[i-2] * 3) + ((temp - dp[i-2]) * 2) + 2
    temp += dp[i]

print(dp[n])