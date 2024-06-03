from collections import deque
import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

def bfs(start):
    queue = deque([start])  # 시작점을 큐에 추가
    while queue:
        current = queue.popleft()  # 현재 탐색할 문자열
        if current == S:
            print(1)
            return
        if len(current) > len(S):
            if current[-1] == 'A':
                queue.append(current[:-1])  # 마지막 'A' 제거
            if current[0] == 'B':
                queue.append(current[:0:-1])  # 첫 번째 'B' 제거 후 뒤집기
    print(0)

bfs(T)
