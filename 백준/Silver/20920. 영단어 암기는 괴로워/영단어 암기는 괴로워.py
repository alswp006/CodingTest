import sys
from collections import Counter

input=sys.stdin.readline
n,m=map(int,input().split())
arr=[]
for i in range(n):
    a=input().rstrip()
    if len(a)<m:continue
    arr.append(a)
arr=Counter(arr)
arr=sorted(arr.items(),key=lambda x :(-x[1],-len(x[0]),x[0]))
for i in arr:print(i[0])