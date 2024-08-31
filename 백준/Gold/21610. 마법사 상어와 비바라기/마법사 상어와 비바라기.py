import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

left_move = {1, 2, 8}
right_move = {4, 5, 6}
up_move = {2, 3, 4}
down_move = {6, 7, 8}
goorm = [(n - 1) * n, (n - 1) * n + 1, (n - 2) * n, (n - 2) * n + 1]
move_type = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

def move_left(num):
    for i in range(len(goorm)):
        if goorm[i] % n - num % n < 0:
            goorm[i] += n
        goorm[i] -= num % n


def move_right(num):
    for i in range(len(goorm)):
        if goorm[i] % n + num % n >= n:
            goorm[i] -= n
        goorm[i] += num % n

def move_up(num):
    for i in range(len(goorm)):
        if goorm[i] // n - num % n < 0:
            goorm[i] += n * n
        goorm[i] -= num % n * n


def move_down(num):
    for i in range(len(goorm)):
        if goorm[i] // n + num % n >= n:
            goorm[i] -= n * n
        goorm[i] += num % n * n


def move_goorm(type, num):
    if type in left_move:
        move_left(num)
    elif type in right_move:
        move_right(num)
    if type in up_move:
        move_up(num)
    elif type in down_move:
        move_down(num)


def rain():
    for i in goorm:
        x, y = i // n, i % n
        arr[x][y] += 1


def water_bug():
    for i in goorm:
        x, y = i // n, i % n
        for dx, dy in move_type:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] > 0:
                arr[x][y] += 1


def create_goorm(goorm):
    s = set(goorm)
    goorm = []
    for i in range(n * n):
        if i in s:
            continue
        x, y = i // n, i % n
        if arr[x][y] >= 2:
            arr[x][y] -= 2
            goorm.append(i)
    return goorm

for i in range(m):
    type, num = map(int,input().split())
    move_goorm(type, num)
    rain()
    water_bug()
    goorm = create_goorm(goorm)

print(sum(sum(i) for i in arr))
