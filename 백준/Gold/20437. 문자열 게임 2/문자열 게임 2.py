import sys

input = sys.stdin.readline

for i in range(int(input())):
    s = input().rstrip()
    k = int(input())
    if len(s) == 1:
        print(1, 1)
        continue
    d = dict()
    s_list = []

    for j in range(len(s)):
        if s[j] in d:
            d[s[j]].append(j)
        else:
            d[s[j]] = [j]
            s_list.append(s[j])

    answer = [10**10, 0]

    for j in s_list:
        if len(d[j]) < k:
            continue
        for r in range(k - 1, len(d[j])):
            temp = d[j][r] - d[j][r - k + 1] + 1
            answer[0] = min(answer[0], temp)
            answer[1] = max(answer[1], temp)

    if answer[0] == 10**10:
        print(-1)
    else:
        print(answer[0], answer[1])