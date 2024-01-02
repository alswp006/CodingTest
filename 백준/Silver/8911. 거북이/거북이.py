import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction = (direction - 1) % 4
    return 0,0

def turn_right():
    global direction
    direction = (direction + 1) % 4
    return 0,0

def move_forward(x, y):
    x, y = x + dx[direction], y + dy[direction]
    return x, y

def move_backward(x, y):
    x, y = x - dx[direction], y - dy[direction]
    return x, y

for _ in range(int(input())):
    x, y = 0, 0
    direction = 0
    x_set, y_set = {0}, {0}

    move = {'L': turn_left, 'R': turn_right, 'F': move_forward, 'B': move_backward}

    for move_type in input().rstrip():
        if move_type in ['F', 'B']:
            x, y = move[move_type](x, y)
            x_set.add(x)
            y_set.add(y)
        else:
            move[move_type]()

    print((max(x_set) - min(x_set)) * (max(y_set) - min(y_set)))