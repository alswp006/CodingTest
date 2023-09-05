import sys

input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
answer=0

arr.sort()

for i in range(1,n+1):
    answer+=arr.pop()*i

print(answer)