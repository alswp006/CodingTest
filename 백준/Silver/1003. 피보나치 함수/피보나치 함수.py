import sys

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = 1, 0
    for i in range(int(input())):
        a, b = b, a + b
    print(a, b)
