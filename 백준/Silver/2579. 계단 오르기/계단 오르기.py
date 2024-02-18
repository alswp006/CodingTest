import sys

input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))
answer = [0] * 301

answer[1] = arr[1]
if n > 1:
    answer[2] = arr[1] + arr[2]
if n > 2:
    answer[3] = max(arr[1], arr[2]) + arr[3]
if n > 3:
    for i in range(4, n + 1):
        answer[i] = max(answer[i - 3] + arr[i - 1], answer[i - 2]) + arr[i]
print(answer[n])