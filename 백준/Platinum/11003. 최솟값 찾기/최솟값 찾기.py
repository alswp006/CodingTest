import sys
from collections import deque

input = sys.stdin.readline

n,l = map(int,input().split())
d1 = list(map(int,input().split()))
d2 = deque()

for i in range(n):
    while d2 and d1[i] < d2[-1][-1]:
        d2.pop()
    d2.append((i,d1[i]))
    if d2[0][0] < i-l+1:
        d2.popleft()
    print(d2[0][1],end=' ')