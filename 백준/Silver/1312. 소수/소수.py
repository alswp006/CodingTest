a, b, n = map(int, input().split())
answer = 0

for i in range(n):
    a = a % b * 10
    answer = a // b

print(answer)