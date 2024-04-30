import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())
x, y, d = map(int,input().split())
move = deque([[-1, 0], [0, 1], [1, 0], [0, -1]])
room = [list(map(int,input().split())) for i in range(n)]
answer = 0
flag = 1

for i in range(d):
    move.append(move.popleft())

while flag:
    if room[x][y] == 0:
        room[x][y] = 2
        answer += 1
    for i in range(4):
        move.appendleft(move.pop())
        dx, dy = move[0]
        nx, ny = x + dx, y + dy
        if room[nx][ny] == 0:
            x, y = nx, ny
            break
    else:
        dx, dy = move[2]
        x, y = x + dx, y + dy
        if room[x][y] == 1:
            flag = 0

print(answer)
