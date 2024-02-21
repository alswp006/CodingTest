n = int(input())

a = 1
b = 2

for i in range(3, n + 1):
    a, b = b, (a+b)%15746

print(b if n != 1 else 1)