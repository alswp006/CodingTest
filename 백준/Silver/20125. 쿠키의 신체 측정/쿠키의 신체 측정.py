import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input().rstrip())
arr=[[0 for i in range(n)] for i in range(n)]
temp=0
for i in range(n):
    a=input().rstrip()
    for j in range(len(a)):
        if a[j]=='*':
            arr[i][j]=1
            temp+=1
        if a[j]=='*' and temp==1:
            arr[i][j]=0
            x,y=i+1,j
arr[x][y]=0
print(f"{x+1} {y+1}")
def dfs(x,y):
    global count
    if x<0 or y<0 or x>=n or y>=n:return False
    if arr[x][y]==0: return False
    count+=1
    arr[x][y]=0
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            count=0
            dfs(i,j)
            print(count,end=' ')