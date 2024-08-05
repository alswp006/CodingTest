from collections import deque

n, k = map(int, input().split())
limit = 100001
cnt = [0] * limit
visited = [False] * limit
queue = deque([n])

while queue:
    x = queue.popleft()
    if x == k:
        print(cnt[x])
        break
    if -1 < x * 2 < limit and not visited[x * 2]:
        queue.appendleft(x * 2)
        cnt[x * 2] = cnt[x]
        visited[x * 2] = True
    if -1 < x - 1 < limit and not visited[x - 1]:
        queue.append(x - 1)
        cnt[x - 1] = cnt[x] + 1
        visited[x - 1] = True
    if -1 < x + 1 < limit and not visited[x + 1]:
        queue.append(x + 1)
        cnt[x + 1] = cnt[x] + 1
        visited[x + 1] = True
