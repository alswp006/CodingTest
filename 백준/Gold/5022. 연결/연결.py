import sys
from collections import deque

input = sys.stdin.readline

# 상수 정의
MAX = 101
INF = 999999999
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 전역 변수
N, M = 0, 0
Answer = INF
A_Length, B_Length = 0, 0
A_Flag, B_Flag, Answer_Flag = False, False, False

# 전선 상태 저장: 0 - 없음, 1 - A전선, 2 - B전선
Visit = [[0]*(MAX) for _ in range(MAX)]
Temp_Visit = [[False]*(MAX) for _ in range(MAX)]

A_Pos = [(0,0),(0,0)]
B_Pos = [(0,0),(0,0)]

def Min(a, b):
    return a if a < b else b

def Input():
    global N, M
    M, N = map(int, input().split())
    # A의 두 점 입력
    for i in range(2):
        x, y = map(int, input().split())
        A_Pos[i] = (y, x)  # (row = y, col = x)
    # B의 두 점 입력
    for i in range(2):
        x, y = map(int, input().split())
        B_Pos[i] = (y, x)

def bfs(a, b, da, db, c):
    global A_Flag, B_Flag, A_Length, B_Length
    # 부모 정보 저장용 배열
    parent = [[(-1, -1) for _ in range(M+1)] for __ in range(N+1)]
    for i in range(N+1):
        for j in range(M+1):
            Temp_Visit[i][j] = False

    q = deque()
    q.append((a, b))
    Temp_Visit[a][b] = True

    # 시작점에 대한 Visit 설정
    if c == 'A':
        Visit[a][b] = 1
    else:
        Visit[a][b] = 2

    while q:
        x, y = q.popleft()
        if x == da and y == db:
            # 도착 지점에 도달: 경로 복원
            route = []
            cx, cy = da, db
            while cx != -1 and cy != -1:
                route.append((cx,cy))
                cx, cy = parent[cx][cy]
            route.reverse()

            # 경로 표시 및 길이 계산
            if c == 'A':
                A_Flag = True
                for (rx, ry) in route:
                    Visit[rx][ry] = 1
                A_Length += len(route)
            else:
                B_Flag = True
                for (rx, ry) in route:
                    Visit[rx][ry] = 2
                B_Length += len(route)

            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > N or ny > M:
                continue

            # A 깔 때: B의 두 점은 통과 불가
            # B 깔 때: A의 두 점은 통과 불가
            if c == 'A':
                if (nx, ny) == B_Pos[0] or (nx, ny) == B_Pos[1]:
                    continue
                # 이미 방문 or 다른 전선이 깔려있으면 불가
                if Temp_Visit[nx][ny] or Visit[nx][ny] != 0:
                    continue
            else:
                if (nx, ny) == A_Pos[0] or (nx, ny) == A_Pos[1]:
                    continue
                if Temp_Visit[nx][ny] or Visit[nx][ny] != 0:
                    continue

            Temp_Visit[nx][ny] = True
            parent[nx][ny] = (x, y)
            q.append((nx, ny))

def Solution():
    global A_Flag, B_Flag, A_Length, B_Length, Answer, Answer_Flag

    # 초기 A->B 순서로 전선 깔기
    x, y = A_Pos[0]
    xx, yy = A_Pos[1]
    bfs(x, y, xx, yy, 'A')

    # A BFS 후 Temp_Visit 초기화는 bfs 함수 내에서 처리
    x, y = B_Pos[0]
    xx, yy = B_Pos[1]
    bfs(x, y, xx, yy, 'B')

    if A_Flag and B_Flag:
        Answer_Flag = True
        Answer = Min(Answer, A_Length + B_Length)

    # 상태 초기화
    for i in range(N+1):
        for j in range(M+1):
            Visit[i][j] = 0
    A_Length, B_Length = 0, 0
    A_Flag, B_Flag = False, False

    # B->A 순서로 전선 깔기
    x, y = B_Pos[0]
    xx, yy = B_Pos[1]
    bfs(x, y, xx, yy, 'B')

    x, y = A_Pos[0]
    xx, yy = A_Pos[1]
    bfs(x, y, xx, yy, 'A')

    if A_Flag and B_Flag:
        Answer_Flag = True
        Answer = Min(Answer, A_Length + B_Length)

def Solve():
    Input()
    Solution()

    if not Answer_Flag:
        print("IMPOSSIBLE")
    else:
        # C++ 코드와 동일하게 출력 (Answer - 2)
        # 이는 문제 출처에 따른 요구사항으로 보임.
        print(Answer - 2)

if __name__ == "__main__":
    Solve()