from collections import deque

arr = [deque(map(int,input())) for i in range(4)]
k = int(input())

def left_rotate(n, prev_left, rotate_num):
    if arr[n][2] == prev_left:
        return
    prev_left = arr[n][6]
    rotate(n, rotate_num)

    if n == 0:
        return

    left_rotate(n - 1, prev_left, rotate_num * (-1))
    return

def right_rotate(n, prev_right, rotate_num):
    if arr[n][6] == prev_right:
        return
    prev_right = arr[n][2]
    rotate(n, rotate_num)

    if n == 3:
        return

    right_rotate(n + 1, prev_right, rotate_num * (-1))
    return

def rotate(n, rotate_num):
    if rotate_num == 1:
        arr[n].appendleft(arr[n].pop())
    else:
        arr[n].append(arr[n].popleft())

for i in range(k):
    n, rotate_num = map(int,input().split())
    n -= 1
    if n == 0:
        right_rotate(n + 1, arr[n][2], rotate_num * (-1))
    elif n == 3:
        left_rotate(n - 1, arr[n][6], rotate_num * (-1))
    else:
        right_rotate(n + 1, arr[n][2], rotate_num * (-1))
        left_rotate(n - 1, arr[n][6], rotate_num * (-1))
    rotate(n,rotate_num)

answer = 0

for i in range(4):
    if arr[i][0] == 1:
        answer += 2 ** i

print(answer)