n, m = map(int, input().split())
a, b = n, m
while b != 0:
    a, b = b, a % b

print(n * m // a)