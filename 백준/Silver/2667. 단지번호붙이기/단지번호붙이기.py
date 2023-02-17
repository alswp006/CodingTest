from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
arr=[]
num=0
for i in range(n):
    arr.append(list(map(int,input().rstrip())))

def dfs(x,y):
    global answer
    if x<0 or y<0 or x>=n or y>=n:return False
    if arr[x][y]==1:
        arr[x][y]=0
        answer+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
result=[]
for i in range(n):
    for j in range(n):
        answer=0
        if dfs(i,j)==True:
            num+=1
            result.append(answer)
result.sort()
print(num)
for i in result:print(i)