import sys

input = sys.stdin.readline

n, lim = map(int, input().split())

level, id = input().rstrip().split()
room = [[[int(level), id]]]

for _ in range(n - 1):
    level, id = input().rstrip().split()
    level = int(level)

    for i in range(len(room)):
        room_level = room[i][0][0]
        if len(room[i]) == lim:
            continue
        if max(level, room_level) - min(level, room_level) <= 10:
            room[i].append([level, id])
            break
    else:
        room.append([[level, id]])

for i in range(len(room)):
    print("Started!" if len(room[i]) == lim else "Waiting!")
    for j in sorted(room[i], key=lambda x: x[1]):
        print(*j)
