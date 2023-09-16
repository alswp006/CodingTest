import sys

input=sys.stdin.readline

arr=[]
answer=0
temp=0
temp_sum=0

for _ in range(int(input())):
    arr.append(int(input()))

arr.sort()

for i in range(len(arr)):
    temp=arr[-i-1]*(i+1)
    answer=max(answer,temp)

print(answer)