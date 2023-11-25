import bisect

n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in arr:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect.bisect_left(dp, i)] = i

print(len(dp) - 1)