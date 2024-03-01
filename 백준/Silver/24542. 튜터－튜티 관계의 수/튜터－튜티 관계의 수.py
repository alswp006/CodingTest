import sys

input = sys.stdin.readline

def find(x):    # 유니온 파인드의 find 함수
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):    # 유니온 파인드의 union 함수
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        size[x] += size[y]

n,m = map(int,input().split())
parent = list(range(n+1))    # 각 노드의 부모 노드 정보를 저장하는 리스트
size = [1] * (n+1)    # 각 노드를 루트로 하는 서브트리의 크기를 저장하는 리스트

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

answer = 1
for i in range(1, n+1):
    if parent[i] == i:    # 루트 노드만 고려
        answer *= size[i]

print(answer%1000000007)
