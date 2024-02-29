import sys

input = sys.stdin.readline

n = int(input())
jump = list(map(int,input().split()))
answer = [1002] * n
answer[0] = 0

for i in range(len(jump)):
    if answer == 1002:
        continue
    for j in range(1, jump[i] + 1):
        if i + j < n:
            answer[i+j] = min(answer[i+j], answer[i] + 1)

print(answer[-1] if answer[-1] != 1002 else -1)