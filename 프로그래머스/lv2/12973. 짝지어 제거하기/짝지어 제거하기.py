from collections import deque

def solution(s):
    s=deque(s)
    stack=deque()
    if len(s)%2!=0:return 0
    while s:
        c=s.popleft()
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    return 1 if len(stack)==0 else 0 