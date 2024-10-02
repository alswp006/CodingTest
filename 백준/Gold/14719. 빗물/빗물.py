h, w = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    compare = min(max(arr[:i]), max(arr[i + 1:]))
    answer += compare - arr[i] if arr[i] < compare else 0

print(answer)