E, S, M = map(int, input().split())
num = max(E, S, M)

while (num - E) % 15 != 0 or (num - S) % 28 != 0 or (num - M) % 19 != 0:
    num+=1

print(num)