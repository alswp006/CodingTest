import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(input().rstrip())
answer = 0

for i in range(n):
    if arr[i] != "P":
        continue
    range_min = 0 if i - k < 0 else i - k
    range_max = n if i + k > n - 1 else i + k + 1
    
    for j in range(range_min, range_max):
        if arr[j] == "H":
            answer += 1
            arr[j] = "X"
            break
print(answer)