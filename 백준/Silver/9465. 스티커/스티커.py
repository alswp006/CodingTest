import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [[] for i in range(n)]
    for _ in range(2):
        n = 0
        for i in list(map(int,input().split())):
            arr[n].append(i)
            n+=1
    dp = [[0, 0] for _ in range(n)]

    if n == 1:
        print(max(arr[0]))
        continue
    else:
        dp[0][0] = arr[0][0]
        dp[0][1] = arr[0][1]
        dp[1][0] = dp[0][1] + arr[1][0]
        dp[1][1] = dp[0][0] + arr[1][1]
        
    for i in range(2, n):
        for j in range(2):
            dp[i][j] = max(dp[i-1][abs(j-1)], dp[i-2][abs(j-1)]) + arr[i][j]
    print(max(dp[-1]))