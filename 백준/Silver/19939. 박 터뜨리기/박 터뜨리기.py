n, k = map(int,input().split())

for i in range(k):
    n -= i + 1

if n < 0:
    print(-1)
elif n == 0:
    print(k - 1)
else:
    if n % k > 0: print(k)
    else: print(k - 1)
