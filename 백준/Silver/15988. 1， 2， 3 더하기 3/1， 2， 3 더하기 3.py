dp=[0,1,2,4] + [0] * 1000000

for i in range(4,len(dp)):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
for _ in range(int(input())):
    print(dp[int(input())])