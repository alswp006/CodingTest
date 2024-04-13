import sys
from collections import deque

input = sys.stdin.readline

q = deque(input().rstrip())
zero_lim = q.count("0") // 2
one_lim = q.count("1") // 2
current_zero = 0
current_one = 0

answer = []

while q:
    temp = q.popleft()

    if temp == "0" and current_zero < zero_lim:
        current_zero += 1
        answer.append(temp)
    elif temp == "1" and current_one >= one_lim:
        answer.append(temp)
    elif temp == "1":
        current_one += 1

print(''.join(answer))