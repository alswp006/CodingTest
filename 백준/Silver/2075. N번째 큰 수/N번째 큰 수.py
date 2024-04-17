import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) # 첫 줄 초기화
heapq.heapify(arr) # 힙으로 변환

for _ in range(n - 1):
    nums = map(int,input().split())
    for i in nums:
        heapq.heappush(arr, i)
        heapq.heappop(arr)
        
print(arr[0])