import sys

input = sys.stdin.readline

arr = [[0 for _ in range(101)] for _ in range(101)]
answer=0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j]=1
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]==1:
            answer+=1
print(answer)