n = int(input())

answer, p, s = 0, 1, 1

while s <= n:
    if not (n - s) % p: answer += 1
    p += 1
    s += p
print(answer)