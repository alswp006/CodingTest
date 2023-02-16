import sys
from collections import deque

input=sys.stdin.readline

left=deque(input().rstrip())
right=deque()
for _ in range(int(input())):
    arr=input().split()
    if arr[0]=='L' and len(left)!=0:
        right.appendleft(left.pop())
    elif arr[0]=='D' and len(right)!=0:
        left.append(right.popleft())
    elif arr[0]=='B' and len(left)!=0:
        left.pop()
    elif arr[0]=='P':
        left.append(arr[1])
sys.stdout.write(''.join(left+right))