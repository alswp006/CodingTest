import sys
import itertools

input = sys.stdin.readline

while True:
    li=list(map(str,input().split()))
    if len(li)==1:break
    li=li[1:]
    for i in itertools.combinations(li,6):
        print(' '.join(i))
    print()