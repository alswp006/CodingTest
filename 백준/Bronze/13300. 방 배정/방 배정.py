import sys

input = sys.stdin.readline

n,k = map(int,input().split())
arr = [[0,0] for _ in range(6)]
count = 0

for _ in range(n):
    gender, grade = map(int,input().split())
    arr[grade-1][gender] += 1
    if arr[grade-1][gender] == k:
        arr[grade-1][gender] = 0
        count += 1
for i in arr:
    for j in i:
        if j > 0:
            count+=1
print(count)