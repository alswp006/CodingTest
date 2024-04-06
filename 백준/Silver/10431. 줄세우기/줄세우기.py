import sys
input = sys.stdin.readline

def find(x):
    temp = 0
    for i in range(x, 1, -1):
        if arr[i] > arr[i - 1]:
            return temp
        temp += 1
        arr[i], arr[i-1] = arr[i-1], arr[i]
    return temp


for i in range(int(input())):
    answer = 0
    arr = list(map(int, input().split()))
    for i in range(2, len(arr)):
        if arr[i] < arr[i - 1]:
            answer += find(i)
    print(arr[0], answer)