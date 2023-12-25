import sys

input()
arr = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(len(arr)):
    if arr[i] != i + 1:
        print(i + 1)
        exit()
print(len(arr) + 1)