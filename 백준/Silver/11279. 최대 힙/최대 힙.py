import heapq
import sys

input=sys.stdin.readline
heap=[]

for i in range(int(input())):
    n=int(input())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            m=heapq.heappop(heap)
            print(m[1])
    else:
        heapq.heappush(heap, (-n,n))