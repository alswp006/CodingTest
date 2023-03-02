from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maxx,maxy=0,0
    for i in rectangle:
        maxx=max(maxx,i[2]*2)
        maxy=max(maxy,i[3]*2)
    arr=[[0 for i in range(maxx+3)] for i in range(maxy+2)]
    for rec in rectangle:
        for i in range(rec[0]*2,rec[2]*2+1):
            for j in range(rec[1]*2,rec[3]*2+1):
                arr[j][i]=1
    dx=[1,0,0,-1,1,-1,-1,1]
    dy=[0,1,-1,0,1,1,-1,-1]
    for y in range(1,maxy + 1):
        for x in range(1,maxx + 1):
            for i in range(3):
                for j in range(3):
                    if arr[y + i - 1][x + j - 1] == 0 and arr[y][x] == 1:
                        arr[y][x]=2
                        break
    q=deque()
    ix=itemX*2
    iy=itemY*2
    q.append([characterX*2,characterY*2,0])
    while q:
        x,y,k=q.popleft()
        arr[y][x]=1
        if x==ix and y==iy:
                answer=k//2
                break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if arr[ny][nx]==2:
                q.append([nx,ny,k+1])
    return answer