import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_num = max(map(max, board))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def dfs(r, c, cnt, res):
    global answer
    if res + (4 - cnt) * max_num < answer:
        return
    
    if cnt == 4:
        answer = max(answer, res)
        return
    
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0:
            temp = board[nr][nc]
            if cnt == 2:
                board[nr][nc] = 0
                dfs(r, c, cnt + 1, res + temp)
                board[nr][nc] = temp
            
            board[nr][nc] = 0
            dfs(nr, nc, cnt + 1, res + temp)
            board[nr][nc] = temp
    
def solution():
    for i in range(N):
        for j in range(M):
            temp = board[i][j]
            board[i][j] = 0
            dfs(i, j, 1, temp)
            board[i][j] = temp
    return answer

print(solution())