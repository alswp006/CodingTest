import sys

input = sys.stdin.readline

for _ in range(int(input())):
    int(input())
    arr = sorted(list(map(int,input().split())))
    sum = 0

    for i in range(1,len(arr)):
        sum += arr[i] - arr[i-1]

    print(sum * 2)