from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    left = deque()
    right = deque()

    for i in list(input().rstrip()):
        if i == "<":
            if left:
                right.appendleft(left.pop())
        elif i ==  ">":
            if right:
                left.append(right.popleft())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left + right))