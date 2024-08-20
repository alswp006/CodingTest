n, k = map(int,input().split())
n -= ((1 + k) * k // 2)
print(-1 if n < 0 else k - 1 if n % k == 0 else k)
