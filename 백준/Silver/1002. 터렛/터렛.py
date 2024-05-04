import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))

    dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if dis == 0 and r1 == r2:
        print(-1)
        continue
    if dis != 0:
        if r1 + r2 == dis or abs(r2 - r1) == dis:
            print(1)
            continue
        elif ((abs(r1 - r2) < dis) and (dis < r1 + r2)):
            print(2)
            continue
    print(0)