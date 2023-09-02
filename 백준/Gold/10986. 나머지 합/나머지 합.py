import sys
from collections import deque

'''sys.stdin = open("input.txt")'''
input = sys.stdin.readline


n,m=map(int,input().rstrip().split())
arr=[0]+list(map(int,input().split()))
answer=0
notZero=[0]*m

for i in range(1,n+1):
    arr[i]+=arr[i-1]
    if arr[i]%m==0:
        answer+=1
    else:
        notZero[arr[i]%m]+=1
answer += ((answer*(answer-1))//2)

for i in notZero:
    if i>1:
        answer += ((i*(i-1)) // 2)

print(answer)