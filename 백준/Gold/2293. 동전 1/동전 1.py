import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
answer = [1] + [0] * (k + 1)

for i in arr:
    for j in range(i, k + 1):
        answer[j] += answer[j - i]

print(answer[k])