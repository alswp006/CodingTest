n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = -1000000

for i in range(m, len(arr) + 1):
    answer = max(answer, sum(arr[i - m: i]))

print(answer)