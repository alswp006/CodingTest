s1 = input()
s2 = input()
l_s1 = len(s1)
l_s2 = len(s2)
dp = [[''] * len(s1) for _ in range(len(s2))]

flag = False
for i in range(l_s1):
    if s2[0] == s1[i]:
        flag=True
    if flag:
        dp[0][i] = s2[0]

flag = False
for i in range(l_s2):
    if s1[0] == s2[i]:
        flag = True
    if flag:
        dp[i][0] = s1[0]

for i in range(1, l_s2):
    for j in range(1, l_s1):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i - 1][j - 1] + s1[j]
            continue
        dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

print(len(dp[-1][-1]))
print(dp[-1][-1])