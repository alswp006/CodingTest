import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
answer = 0


def horizontal_dfs(x, y):
    global answer
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 1:
        return False
    if x == n - 1 and y == n - 1:
        answer += 1
        return True
    horizontal_dfs(x, y + 1)
    diagonal_dfs(x + 1, y + 1)
    return


def vertical_dfs(x, y):
    global answer
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 1:
        return False
    if x == n - 1 and y == n - 1:
        answer += 1
        return True
    vertical_dfs(x + 1, y)
    diagonal_dfs(x + 1, y + 1)
    return


def diagonal_dfs(x, y):
    global answer
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 1:
        return False
    if arr[x - 1][y] == 1 or arr[x][y - 1] == 1:
        return False
    if x == n - 1 and y == n - 1:
        answer += 1
        return True
    horizontal_dfs(x, y + 1)
    vertical_dfs(x + 1, y)
    diagonal_dfs(x + 1, y + 1)
    return

if arr[-1][-1] == 1:
    print(0)
else:
    horizontal_dfs(0, 1)
    print(answer)
