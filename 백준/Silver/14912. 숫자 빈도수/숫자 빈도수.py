n, m = map(int,input().split())
answer = 0

for i in range(1, n + 1):
    num = str(i)
    for s in num:
        if int(s) == m: answer += 1
print(answer)
