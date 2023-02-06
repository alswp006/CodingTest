from collections import deque
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(x,y):
    return (x*y)//gcd(x,y) 
def solution(arr):
    q=deque(arr)
    while len(q)>1:
        x=q.popleft()
        y=q.popleft()
        q.append(lcm(x,y))
    return q.pop()
