def solution(n, com):
    answer = 0
    def dfs(x):
        for j in range(len(com[x])):
            if com[x][j]==1:
                com[x][j]=0
                dfs(j)
    for i in range(len(com)):
        for j in range(len(com[i])):
            if com[i][j]==1:
                answer+=1
                dfs(i)
                
    return answer