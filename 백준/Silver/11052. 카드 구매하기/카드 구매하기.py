import sys
input = sys.stdin.readline

n=int(input())
data=list(map(int,input().split()))
dp=[0 for i in range(n+1)]
for i in range(1,n+1):
    dp[i]=data[i-1]
    for j in range(i):
        dp[i]=max(dp[i-j]+dp[j],dp[i])
print(dp[-1])