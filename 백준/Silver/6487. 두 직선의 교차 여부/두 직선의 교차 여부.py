import sys

input = sys.stdin.readline


def find_intersection_point(d1, d2, x1, y1, x3, y3):
    # 두 선분의 기울기가 다른 경우, 교차점을 찾는 함수
    X = (y3 - y1 + x1 * d1 - x3 * d2) / (d1 - d2)
    Y = d1 * (X - x1) + y1
    return (X, Y)


n = int(input())

for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if x1 != x2 and x3 != x4:  # 두 선분 모두 기울기가 무한이 아닌 경우
        d1 = (y1 - y2) / (x1 - x2)
        d2 = (y3 - y4) / (x3 - x4)

        if d1 == d2:
            if y3 == d1 * (x3 - x1) + y1:  # 두 선분이 같은 선 위에 있는 경우
                print("LINE")
            else:
                print("NONE")
        else:
            point = find_intersection_point(d1, d2, x1, y1, x3, y3)
            print("POINT {:.2f} {:.2f}".format(point[0], point[1]))

    else:  # 하나 혹은 두 선분의 기울기가 무한인 경우
        if x1 == x2 and x3 == x4:
            if x1 == x3:
                print("LINE")
            else:
                print("NONE")
        else:
            if x1 == x2:
                d2 = (y3 - y4) / (x3 - x4)
                Y = d2 * (x1 - x3) + y3
            else:
                d1 = (y1 - y2) / (x1 - x2)
                Y = d1 * (x3-x1) + y1
            print("POINT {:.2f} {:.2f}".format(x1 if x1 == x2 else x3, Y))