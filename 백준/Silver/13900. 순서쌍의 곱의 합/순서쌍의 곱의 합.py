n = int(input())
arr = list(map(int, input().split()))
result = 0
temp = 0

for i in range(n):
    result += arr[i] * temp
    temp += arr[i]

print(result)