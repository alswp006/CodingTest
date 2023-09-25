import sys

input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

answer = 1
distance = 0
arr.sort()

for i in range(1, n):
    distance += arr[i] - arr[i-1]
    if m > distance:continue
    else:
        answer += 1
        distance = 0
print(answer)