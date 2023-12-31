import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction


def turn_right(direction):
    direction += 1
    if direction > 3:
        direction = 0
    return direction


for _ in range(int(input())):
    x, y = 0, 0
    direction = 0
    move_types = input().rstrip()
    right_max = 0
    left_max = 0
    down_max = 0
    up_max = 0

    for move_type in move_types:
        if move_type == 'L':
            direction = turn_left(direction)
        elif move_type == 'R':
            direction = turn_right(direction)
        elif move_type == 'F':
            x = x + dx[direction]
            y = y + dy[direction]
        elif move_type == 'B':
            x = x - dx[direction]
            y = y - dy[direction]
        right_max = max(x, right_max)
        left_max = min(x, left_max)
        up_max = min(y, up_max)
        down_max = max(y, down_max)
    print((right_max - left_max) * (down_max - up_max))