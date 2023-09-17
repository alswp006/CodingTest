import sys

input = sys.stdin.readline

def find(i):
    if i!=arr[i]:
        arr[i]=find(arr[i])
    return arr[i]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        arr[b]=a
    else:
        arr[a]=b

n,m=map(int,input().split())
arr=[i for i in range(n+1)]
graph=[]
answer=0

for i in range(m):
    a,b,c=map(int,input().split())
    graph.append([c,a,b]) #a,b,c 순서로 해주고 sort(lambda x:x[2])써도 되지만 그냥 sort쓰는게 편할거같아서 c,a,b 순으로 넣음

graph.sort()

for c,a,b in graph:
    #싸이클 판별
    if find(a)!=find(b):
        union(a,b)
        answer+=c
        last=c
answer-=last

print(answer)