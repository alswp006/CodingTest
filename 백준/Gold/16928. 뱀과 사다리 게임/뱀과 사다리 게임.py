import sys
from collections import deque

input = sys.stdin.readline
arr = [i for i in range(107)]
answer = 10**10
q = deque()
q.append(1)
nm = [0] * 101

n, m = map(int, input().split())

for i in range(n + m):
    x, y = map(int,input().split())
    arr[x] = y

while q:
    num = q.popleft()
    m_ans = nm[num]
    for i in range(1, 7):
        temp = arr[num + i]
        if temp > 100 :
            continue
        elif temp == 100:
            answer = min(answer, m_ans + 1)
            continue
        if nm[temp] != 0:
            continue
        q.append(temp)
        nm[temp] = m_ans + 1

print(answer)