import sys
from collections import deque
import itertools

input = sys.stdin.readline

while True:
    li=deque(list(map(int,input().split())))
    if li.popleft()==0:break
    nCr = itertools.combinations(li,6)
    for i in list(nCr):
        for j in i:
            print(j,end=' ')
        print()
    print()