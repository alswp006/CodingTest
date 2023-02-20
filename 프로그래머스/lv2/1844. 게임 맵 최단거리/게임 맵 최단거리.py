from collections import deque

def bfs(x,y,maps):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]):continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                q.append((nx,ny))
    return maps[-1][-1]
def solution(maps):
    answer=bfs(0,0,maps)
    return answer if answer!=1 else -1