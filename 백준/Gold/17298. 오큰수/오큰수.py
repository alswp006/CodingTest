import sys

input = sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
answer=[0]*n
li=[] #index를 담음

for i in range(n):
    while li and arr[li[-1]] < arr[i]:
        answer[li.pop()] = arr[i]
    li.append(i)
        
while li:
    answer[li.pop()] = -1

for i in answer : print(i,end=' ')