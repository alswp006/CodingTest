import sys
from bisect import bisect_left,bisect_right

input=sys.stdin.readline

n= input()
num= [i for i in input().split()]
m= input()
num2=[i for i in input().split()]
dict={}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(' '.join(str(dict[i]) if i in dict else "0" for i in num2))
