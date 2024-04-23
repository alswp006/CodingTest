import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()


def move(r, b):
    answer = 0
    flag = False

    for i in range(n):
        if s[i] == r and flag:
            answer += 1
            continue
        if s[i] == b:
            flag = True

    temp = 0
    flag = False
    for i in range(n - 1, -1, -1):
        if temp > answer:
            break
        if s[i] == r and flag:
            temp += 1
            continue
        if s[i] == b:
            flag = True
    else:
        answer = temp
    return answer


answer = min(move("R", "B"), move("B", "R"))
print(answer)
