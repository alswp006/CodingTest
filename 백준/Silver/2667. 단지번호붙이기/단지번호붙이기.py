import sys

input = sys.stdin.readline

arr = [list(map(int, input().rstrip())) for i in range(int(input()))]

answer = []


def find(x, y):
    global count
    if x < 0 or y < 0 or x >= len(arr) or y >= len(arr):
        return False
    if arr[x][y] == 0:
        return False

    arr[x][y] = 0
    count += 1
    find(x + 1, y)
    find(x - 1, y)
    find(x, y - 1)
    find(x, y + 1)


for i in range(len(arr)):
    for j in range(len(arr[i])):
        count = 0
        if arr[i][j] == 1:
            find(i, j)
            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i)