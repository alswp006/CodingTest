import copy
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline


def count_zero():
    count = 0

    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 0:
                count += 1
    return count


def dfs(x, y):
    if x >= n or y >= m or x < 0 or y < 0: return
    if temp_arr[x][y] != 0: return
    temp_arr[x][y] = 2

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

    return


def start_dfs(x, y):
    if x - 1 >= 0: dfs(x - 1, y)
    if x + 1 < n: dfs(x + 1, y)
    if y - 1 >= 0: dfs(x, y - 1)
    if y + 1 < m: dfs(x, y + 1)


answer = 0
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
basic_coordinates = []
temp_arr = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0: basic_coordinates.append([i, j])
coordinates = combinations(basic_coordinates, 3)

for i in coordinates:
    temp_arr = copy.deepcopy(arr)
    for x, y in i:
        temp_arr[x][y] = 1

    for x in range(n):
        for y in range(m):
            if temp_arr[x][y] == 2:
                start_dfs(x, y)

    answer = max(answer, count_zero())
print(answer)
