import sys

input = sys.stdin.readline

d = [False, False] + [True] * (123457 * 2 + 1)

for i in range(2, int(len(d) ** 0.5)+1):
    if d[i]:
        for j in range(i * 2, len(d), i):
            d[j] = False

while True:
    n = int(input())
    count = 0

    if n == 0:
        break

    for i in range(n + 1, 2 * n + 1):
        if d[i]:
            count += 1

    print(count)
