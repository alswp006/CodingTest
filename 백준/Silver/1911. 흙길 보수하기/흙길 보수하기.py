import sys
import math
input=sys.stdin.readline

answer=0
arr=[]
n,m=map(int,input().split())
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
for i in range(len(arr)-1):
    temp=arr[i][0]+(m*math.ceil((arr[i][1]-arr[i][0])/m))
    answer+=math.ceil((arr[i][1]-arr[i][0])/m)
    if temp>arr[i+1][0]:
        arr[i+1][0]=temp
answer+=math.ceil((arr[-1][1]-arr[-1][0])/m)
print(answer)