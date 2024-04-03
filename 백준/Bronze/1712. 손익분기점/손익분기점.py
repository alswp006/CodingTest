a, b, c = map(int,input().split())

if b >= c:
    print(-1)
    exit()
print(a // (c - b) + 1)
