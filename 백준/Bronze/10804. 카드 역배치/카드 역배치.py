import sys

input = sys.stdin.readline
arr = [i + 1 for i in range(20)]

for i in range(10):
    n, m = map(int, input().split())
    temp1 = arr[:n - 1]
    temp2 = arr[n - 1:m]
    temp3 = arr[m:]
    temp2.reverse()
    arr = temp1 + temp2 + temp3

for i in arr: print(i, end = ' ')