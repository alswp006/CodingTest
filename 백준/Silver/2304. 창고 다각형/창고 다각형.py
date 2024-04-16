import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
pillar = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x: x[0])
prev_x, prev_y = pillar[0]
temp_li = deque()
answer = 0

for i in range(1, n):
    cur_x, cur_y = pillar[i]
    if cur_y < prev_y:
        temp_li.append([cur_x, cur_y])
        continue
    temp_li = deque()
    answer += (cur_x - prev_x) * prev_y
    prev_x, prev_y = cur_x, cur_y

if temp_li:
    temp_li.appendleft([prev_x, prev_y])
    prev_x, prev_y = temp_li.pop()
    while temp_li :
        cur_x, cur_y = temp_li.pop()
        if cur_y < prev_y:
            continue
        answer += (prev_x - cur_x) * prev_y
        prev_x, prev_y = cur_x, cur_y
    answer += prev_y
else:
    answer += prev_y

print(answer)



