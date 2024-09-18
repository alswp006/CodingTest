import heapq
import sys

input = sys.stdin.readline


def dijkstra(start_v):
    hq = []
    heapq.heappush(hq, [0, start_v])
    distance[start_v] = 0

    while hq:
        now_dis, now_v = heapq.heappop(hq)
        if now_dis > distance[now_v]:
            continue

        for next_v in graph[now_v]:
            next_dis = now_dis + next_v[0]
            if next_dis < distance[next_v[1]]:
                distance[next_v[1]] = next_dis
                heapq.heappush(hq, [next_dis, next_v[1]])


N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    _v1, _v2, c = map(int, input().split())
    graph[_v1].append([c, _v2])
    graph[_v2].append([c, _v1])

v1, v2 = map(int, input().split())

min_dis = [10 ** 9, 10 ** 9]

distance = [10 ** 9] * (N + 1)
distance[1] = 0
dijkstra(1)

if distance[v1] == 10 ** 9 or distance[v2] == 10 ** 9 or distance[N] == 10 ** 9:
    print(-1)
    exit(0)

min_dis[0] = distance[v1]
min_dis[1] = distance[v2]

distance = [10 ** 9] * (N + 1)
distance[v1] = 0
dijkstra(v1)

min_dis[0] += distance[v2]
min_dis[1] += distance[v2]

min_dis[1] += distance[N]

distance = [10 ** 9] * (N + 1)
distance[v2] = 0
dijkstra(v2)

min_dis[0] += distance[N]

print(min(min_dis))