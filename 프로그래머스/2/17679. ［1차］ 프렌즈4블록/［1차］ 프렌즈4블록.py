def solution(m, n, board):
    answer = 0
    visited = [[True for i in range(n)] for j in range(m)]
    board = [[board[j][i] for i in range(n)] for j in range(m)]
    while True:
        flag = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] ==board[i+1][j+1] and board[i][j] != "@":
                    visited[i][j] = False
                    visited[i][j+1] = False 
                    visited[i+1][j] = False
                    visited[i+1][j+1] = False
                    flag +=1
                    
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False:
                    board[i][j] = "@"
                    
        if flag == 0 :
            break
            
        for i in range(n):
            count_mi = 0
            for j in range(m):
                if board[j][i] == "@":
                    count_mi += 1
            flag = True
            while flag:
                for j in range(m - 2, -1, -1):
                    if board[j + 1][i] == "@" and board[j][i] != "@":
                        board[j+1][i], board[j][i] = board[j][i], board[j+1][i]
                        visited[j+1][i], visited[j][i] = visited[j][i], visited[j+1][i]
                        break
                else :
                    flag = False
                
        
    for i in board:
            for j in i:
                if j == "@": answer +=1
    return answer