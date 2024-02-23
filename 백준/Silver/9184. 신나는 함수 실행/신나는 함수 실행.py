import sys

input = sys.stdin.readline

a, b, c = 0, 0, 0
answer = 0
di = dict()
di[(0, 0, 0)] = 1
di[(20, 20, 20)] = 1048576


def w(a, b, c):
    if (a, b, c) in di.keys():
        return di[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return di[(0, 0, 0)]

    if a > 20 or b > 20 or c > 20:
        return di[(20, 20, 20)]

    if a < b and b < c:
        di[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return di[(a, b, c)]
    else:
        di[(a, b, c)] = (
                w(a - 1, b, c)
                + w(a - 1, b - 1, c)
                + w(a - 1, b, c - 1)
                - w(a - 1, b - 1, c - 1)
        )
        return di[(a, b, c)]


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
