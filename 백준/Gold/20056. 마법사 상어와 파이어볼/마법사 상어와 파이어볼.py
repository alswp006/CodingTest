import sys

input = sys.stdin.readline

move_type = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r - 1][c - 1].append([m, s, d])

def move_fire():
    temp_arr = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            while arr[x][y]:
                m, s, d = arr[x][y].pop()
                nx, ny = (x + move_type[d][0] * s) % n, (y + move_type[d][1] * s) % n
                temp_arr[nx][ny].append([m, s, d])
    return temp_arr

def divide_fire():
    answer = 0
    for x in range(n):
        for y in range(n):
            if len(arr[x][y]) == 1:
                answer += arr[x][y][0][0]
            elif len(arr[x][y]) >= 2:
                m, s, num = 0, 0, 0
                even, odd = True, True
                while arr[x][y]:
                    temp_m, temp_s, temp_d = arr[x][y].pop()
                    if temp_d % 2 == 0:
                        odd = False
                    else:
                        even = False
                    m += temp_m
                    s += temp_s
                    num += 1
                temp = 0 if even or odd else 1
                if m // 5 > 0:
                    for i in range(temp, 8, 2):
                        arr[x][y].append([m//5, s // num, i])
                answer += m // 5 * 4
    return answer

answer = 0
for i in range(k):
    arr = move_fire()
    answer = divide_fire()

print(answer)

