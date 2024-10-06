a, b = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))

num = 0
for i in range(m):
    num += arr[i] * (a ** (m - i - 1))

result = []
while num > 0:
    result.append(num % b)
    num //= b

print(' '.join(map(str, result[::-1])))
