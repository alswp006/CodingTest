def dfs(k, cnt, dungeons, visited):
    max_count = cnt
    for i in range(len(dungeons)):
        if not (visited & (1 << i)) and k >= dungeons[i][0]:  # 방문하지 않았고, 탐험 가능하면
            max_count = max(max_count, dfs(k - dungeons[i][1], cnt + 1, dungeons, visited | (1 << i)))
    return max_count

def solution(k, dungeons):
    return dfs(k, 0, dungeons, 0)