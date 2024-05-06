import sys

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    answer = "YES"

    while len(s) >= 3:
        for i in range(2, len(s), 2):
            if s[i - 2] == s[i]:
                answer = "NO"
                break
        else:
            s = s[1::2]
            continue
        break
    print(answer)
