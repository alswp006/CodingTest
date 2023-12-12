import sys

input = sys.stdin.readline
for _ in range(int(input())):
    arr = sorted(list(map(int, input().split())))[1:4]
    if arr[-1] - arr[0] >= 4:
        print("KIN")
    else:
        print(sum(arr))