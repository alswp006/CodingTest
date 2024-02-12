import sys

input = sys.stdin.readline

arr = [input().rstrip() for i in range(int(input()))]
answer=[i for i in arr[0]]

for i in range(len(arr[0])):
    for j in range(1, len(arr)):
        if arr[j-1][i] != arr[j][i]:
            answer[i] = "?"

print(''.join(answer))