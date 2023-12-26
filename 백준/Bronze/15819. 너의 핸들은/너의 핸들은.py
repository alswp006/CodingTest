import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = [input().rstrip() for i in range(n)]
arr.sort()
print(arr[m-1])