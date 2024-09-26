n = int(input())
m = int(input())

crash = set()

if m != 0:
    crash = set(map(int, input().split()))
answer = 10**10
if n == 0:
    for i in range(10):
        if i not in crash:
            print(i + 1)
            exit()
if n == 100:
    print(0)
    exit()

for i in range(n, -1, -1):
    if m == 10: break
    if i == 0 and i in crash: break
    temp = i
    flag = True
    while temp > 0:
        num = temp % 10
        if num in crash:
            flag = False
            break
        temp //= 10
    if flag:
        answer = len(str(i)) + n - i
        break

for i in range(n, 1000000):
    if m == 10: break
    temp = i
    flag = True
    while temp > 0:
        num = temp % 10
        if num in crash:
            flag = False
            break
        temp //= 10
    if flag:
        answer = min(answer, len(str(i)) + i - n)
        break

if n > 100:
    answer = min(answer, n - 100)
else:
    answer = min(answer, 100 - n)
print(answer)