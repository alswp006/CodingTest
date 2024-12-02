import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

arr = [[0] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 1

    for j in range(1, i + 1):
        if i - j < 0 or i + j >= n:
            break
        if nums[i - j] != nums[i + j]:
            break
        arr[i - j][i + j] = 1

    if nums[i - 1] == nums[i]:
        arr[i - 1][i] = 1
    else:
        continue

    for j in range(1, i + 1):
        if i - j < 0 or i + j + 1 >= n:
            break
        if nums[i - j] != nums[i + j + 1]:
            break
        arr[i - j][i + j + 1] = 1

for i in range(int(input())):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    print(arr[a][b])
