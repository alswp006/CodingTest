import sys
import heapq

input = sys.stdin.readline
INF = 1e9

n, m, target_distance, start = map(int,input().split())

table = [INF] * (n + 1)
table[start] = 0
arr = [[] for _ in range(n+1)]
heap = []
heapq.heappush(heap, [0, start])
answer=[]

for _ in range(m):
    starting_node, destination_node = map(int,input().split())
    arr[starting_node].append([destination_node,1])

def dijkstra():
    while heap:
        v, w = heapq.heappop(heap)
        for x, y in arr[w]:
            update = y + v
            if update < table[x]:
                table[x] = update
                heapq.heappush(heap, [update, x])

dijkstra()

for i in range(1, len(table)):
    if table[i] == target_distance:
        answer.append(i)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)