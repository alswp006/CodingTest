n, m = map(int,input().split())
arr = [[0] * m for _ in range(n)]
result = 0

def nemo(i):
    global result
    if i == n * m:
        result += 1
        return

    r, c = divmod(i, m)
    if arr[r-1][c] + arr[r][c-1] + arr[r-1][c-1] != 3:
        arr[r][c] = 1
        nemo(i + 1)
        arr[r][c] = 0
    nemo(i + 1)

nemo(0)
print(result)