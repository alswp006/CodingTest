import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    return (direction - 1) % 4

def turn_right(direction):
    return (direction + 1) % 4

def move_forward(x, y, direction):
    return x + dx[direction], y + dy[direction]

def move_backward(x, y, direction):
    return x - dx[direction], y - dy[direction]

for _ in range(int(input())):
    x, y = 0, 0
    direction = 0
    move_types = input().rstrip()
    right_max, left_max = 0, 0
    down_max, up_max = 0, 0

    for move_type in move_types:
        if move_type == 'L':
            direction = turn_left(direction)
        elif move_type == 'R':
            direction = turn_right(direction)
        elif move_type == 'F':
            x, y = move_forward(x, y, direction)
        elif move_type == 'B':
            x, y = move_backward(x, y, direction)
        right_max, left_max = max(x, right_max), min(x, left_max)
        down_max, up_max = max(y, down_max), min(y, up_max)
    print((right_max - left_max) * (down_max - up_max))