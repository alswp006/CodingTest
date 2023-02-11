import sys
from bisect import bisect_left,bisect_right

input=sys.stdin.readline

n= input()
num= [i for i in input().split()]
m= input()
num2=[i for i in input().split()]
num.sort()   
for i in num2:
    ri=bisect_right(num,i)
    le=bisect_left(num,i)
    print(ri-le,end=' ')