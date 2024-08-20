n, k = map(int,input().split())
n -= (1 + k) * k // 2
if n < 0: print(-1)
elif n % k <= 0: print(k - 1)
else: print(k)
