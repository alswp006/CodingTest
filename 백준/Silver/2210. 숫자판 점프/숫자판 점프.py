from collections import deque

arr = []
answer = set()
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(5):
    arr.append(list(map(str, input().split())))


def bfs(x1, y1):
    q = deque()
    q.append((x1, y1, 0, ""))
    while q:
        x, y, count, str = q.popleft()
        str += arr[x][y]
        if count == 5:
            answer.add(str)
            continue
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            q.append((nx, ny, count + 1, str))
    return


for i in range(5):
    for j in range(5):
        bfs(i, j)
        
print(len(answer))