n, m = map(int, input().split())
arr = [[0 for i in range(n + 1)] for j in range(m + 1)]

for i in range(len(arr[1])):
    arr[1][i] = 1

for i in range(2, m + 1):
    for j in range(len(arr[i])):
        arr[i][j] += arr[i][j - 1] + arr[i - 1][j]

print(arr[m][n]%1000000000)