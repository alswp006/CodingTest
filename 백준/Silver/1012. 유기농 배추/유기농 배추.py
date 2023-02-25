import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m:return None
    if d[x][y]==0: return None
    if d[x][y]==1:
        d[x][y]=0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
for _ in range(int(input().rstrip())):
    m,n,k=map(int,input().split())
    d=[[0 for i in range(m)] for _ in range(n)]
    for i in range(k):
        a,b=map(int,input().split())
        d[b][a]=1
    answer=0
    for i in range(n):
        for j in range(m):
            if d[i][j]==1:
                if dfs(i,j):
                    answer+=1
    print(answer)
