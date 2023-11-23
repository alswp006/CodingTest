n, m = map(int, input().split())

answer = 0
arr = set()
s = []

for i in range(n):
    arr.add(input())

for i in range(m):
    s.append(input())

for i in s:
    if i in arr:
        answer += 1

print(answer)