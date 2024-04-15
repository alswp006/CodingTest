import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = set(input().rstrip() for i in range(n))
for i in range(m):
    for j in input().rstrip().split(","):
        if j in memo:
            memo.remove(j)
    print(len(memo))