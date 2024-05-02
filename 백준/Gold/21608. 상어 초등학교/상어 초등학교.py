import sys

input = sys.stdin.readline

n = int(input())
students = dict()
students_seq = []
answer = [[0 for _ in range(n)] for _ in range(n)]
satisfy_point = [[0 for _ in range(n)] for _ in range(n)]
empty_place = [[4 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1:
            empty_place[i][j] -= 1
        if j == 0 or j == n - 1:
            empty_place[i][j] -= 1

for _ in range(n ** 2):
    stu = list(map(int, input().split()))
    students[stu[0]] = set(stu[1:])
    students_seq.append(stu[0])


def empty_move(x, y):
    move = {"north": [-1, 0], "east": [0, 1], "south": [1, 0], "west": [0, -1]}
    if x == 0:
        move.pop("north")
    elif x == n - 1:
        move.pop("south")
    if y == 0:
        move.pop("west")
    elif y == n - 1:
        move.pop("east")

    return move


def empty_del(x, y):
    move = empty_move(x, y)
    for dx, dy in move.values():
        empty_place[x + dx][y + dy] -= 1


def find_place(stu_id):
    max_num = 0
    nx, ny = 0, 0
    for x in range(n):
        for y in range(n):
            if answer[x][y] != 0:
                continue
            temp = 0
            move = empty_move(x, y)
            for dx, dy in move.values():
                if answer[x + dx][y + dy] in students[stu_id]:
                    temp += 1
            if max_num < temp:
                nx, ny = x, y
                max_num = temp
            elif max_num == temp:
                if empty_place[x][y] > empty_place[nx][ny]:
                    nx, ny = x, y
                    max_num = temp

    if max_num + nx + ny == 0:
        temp = find_max_empty()
        flag = True
        for i in range(n):
            for j in range(n):
                if answer[i][j] != 0:
                    continue
                if empty_place[i][j] == temp:
                    nx, ny = i, j
                    flag = False
                    break
            if not flag:
                break
    answer[nx][ny] = stu_id
    empty_del(nx, ny)

def find_max_empty():
    empty_num = 0
    for i in range(n):
        for j in range(n):
            if answer[i][j] == 0:
                empty_num = max(empty_place[i][j], empty_num)
    return empty_num


answer[1][1] = students_seq[0]
empty_del(1, 1)
for i in range(1, len(students_seq)):
    find_place(students_seq[i])

point = 0
for x in range(n):
    for y in range(n):
        temp = 0
        move = empty_move(x, y)
        for dx, dy in move.values():
            if answer[x][y] in students.keys():
                if answer[x + dx][y + dy] in students[answer[x][y]]:
                    temp += 1
        if temp != 0:
            point += 10 ** (temp - 1)

print(point)
