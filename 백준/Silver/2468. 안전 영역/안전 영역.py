import sys
import copy
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
answer=1
def dfs(x,y,h):
    if x<0 or y<0 or x>=n or y>=n:return 1
    if temp[x][y]>h:
        temp[x][y]=0
        dfs(x+1,y,h)
        dfs(x-1,y,h)
        dfs(x,y+1,h)
        dfs(x,y-1,h)
        return 1
    return 0
an=[]
for h in range(1,101):
    sum=0
    temp=copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if temp[i][j]>h:
                dfs(i,j,h)
                sum+=1
    answer=max(answer,sum)
print(answer)