import sys

input = sys.stdin.readline

d = [False for i in range(123457 * 2)]
primes = set()

for i in range(2, len(d)):
  if not d[i]:
    primes.add(i)
    for j in range(2*i, len(d), i):
        d[j] = True

while True:
    n = int(input())
    count = 0

    if n == 0:
        break

    for i in range(n + 1, 2 * n + 1):
        if i in primes:
            count += 1

    print(count)
