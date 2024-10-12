a, b, n = map(int, input().split())
print(a * pow(10, n, 10 * b) // b % 10)