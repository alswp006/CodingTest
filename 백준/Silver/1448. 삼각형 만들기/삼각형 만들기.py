import sys

input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for i in range(n)], reverse=True)

for i in range(len(arr) - 2):
    if arr[i] < arr[i+1] + arr[i+2]:
        print(sum(arr[i:i+3]))
        break
else:
    print(-1)