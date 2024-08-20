n, k = map(int,input().split())

if n % 2 == 0:
    n -= (k + 1) * k // 2
else:
    n -= k * (k//2 + 1)

if n < 0:
    print(-1)
elif n == 0:
    print(k - 1)
else:
    if n % k > 0: print(k)
    else: print(k - 1)
