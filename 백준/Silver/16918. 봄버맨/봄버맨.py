import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def bomb(x, y):
    for dx, dy in move_type:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        arr[nx][ny] = "."


def search(x, y):
    if x < 0 or x >= r or y < 0 or y >= c: return
    if prev_arr[x][y] == ".": return
    prev_arr[x][y] = "."
    arr[x][y] = "."
    bomb(x, y)
    search(x - 1, y)
    search(x + 1, y)
    search(x, y - 1)
    search(x, y + 1)


r, c, n = map(int, input().split())
prev_arr = [list(input().rstrip()) for _ in range(r)]
arr = [temp[:] for temp in prev_arr]
move_type = [(1, 0), (-1, 0), (0, 1), (0, -1)]
count = 1

while count != n:
    arr = [["O" for _ in range(c)] for _ in range(r)]
    if count + 1 == n: break
    for x in range(r):
        for y in range(c):
            if prev_arr[x][y] == "O":
                search(x, y)
    prev_arr = [temp[:] for temp in arr]
    count += 2

for temp in arr:
    print(''.join(temp))
