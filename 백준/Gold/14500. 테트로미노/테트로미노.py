import sys
input = sys.stdin.readline

shape = [
    [(0, 1), (1, 0), (1, 1)],
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (2, 0), (2, -1)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (0, 2), (1, 0)],
    [(0, 1), (0, 2), (-1, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (2, 0)],
    [(0, 1), (0, 2), (-1, 1)],
    [(1, 0), (1, -1), (2, 0)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, -1), (2, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, -1)],
    [(0, 1), (1, 1), (1, 0)],
    [(0, 1), (1, 1), (-1, 1)]
]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

def get_result(x, y):
    global answer
    for i in range(len(shape)):
        result = arr[x][y]
        for dx, dy in shape[i]:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                result += arr[x + dx][y + dy]
                continue
            break
        else:
            answer = max(answer, result)

answer = 0

for i in range(n):
    for j in range(m):
        get_result(i, j)

print(answer)
