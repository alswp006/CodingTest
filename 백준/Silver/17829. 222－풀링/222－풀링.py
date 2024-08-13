import sys

input = sys.stdin.readline

n = int(input())
prev_arr = [list(map(int,input().split())) for _ in range(n)]

while n != 1:
    n //= 2
    arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i].append(sorted([prev_arr[i * 2][j * 2], prev_arr[i * 2 + 1][j * 2], prev_arr[i * 2][j * 2 + 1], prev_arr[i * 2 + 1][j * 2 + 1]])[2])

    prev_arr = [[arr[temp_x][temp_y] for temp_y in range(n)] for temp_x in range(n)]

print(prev_arr[0][0])
