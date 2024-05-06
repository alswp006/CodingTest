import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = sum(arr[:m])
temp = answer
for i in range(1, n - m + 1):
    temp = temp - arr[i - 1] + arr[i + m - 1]
    answer = max(answer, temp)

print(answer)
