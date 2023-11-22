import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

N, D = map(int,input().split())
arr = [[] for _ in range(D+1)]
heap = []
heapq.heappush(heap, [0, 0])
table = [INF] * (D+1)
table[0] = 0

for i in range(N):
    start, end, dist = map(int,input().split())
    if end <= D:
        arr[start].append([dist, end])

for i in range(D):
    arr[i].append([1,i+1])

def dijkstra():
    while heap:
        v, w = heapq.heappop(heap)
        for next_dist, next_node in arr[w]:
            update = next_dist + v
            if update < table[next_node]:
                table[next_node] = update
                heapq.heappush(heap, [update, next_node])

dijkstra()

print(table[D])