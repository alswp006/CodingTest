import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
answer = 0
answer_li = []

def square(x1, y1, x2, y2):
    for i in range(x1, x2):
        for j in range(y2, y1):
            arr[j][i] = 1


def dfs(x, y):
    global temp
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if arr[x][y] == 1:
        return
    arr[x][y] = 1
    temp += 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    return


for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    square(x1, n - y1, x2, n - y2)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            temp = 0
            answer += 1
            dfs(i, j)
            answer_li.append(temp)
print(answer)
print(*sorted(answer_li))