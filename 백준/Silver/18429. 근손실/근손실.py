n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for i in range(n)]
answer = 0


def dfs(day, power):
    global answer

    if power < 500:
        return
    if day + 1 == n:
        answer += 1
        return

    power -= k

    for i in range(n):
        if not visited[i]:
            visited[i] = True 
            dfs(day + 1, power + arr[i])
            visited[i] = False



dfs(0, 500)
print(answer)
