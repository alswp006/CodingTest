import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
arr = [int(input()) for i in range(n)] * 2
answer = 0
for i in range(n):
    s = set(arr[i:i+k])
    temp = len(s) + 1 if c not in s else len(s)
    answer = max(answer, temp)

print(answer)