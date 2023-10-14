import sys
input = sys.stdin.readline

arr=sorted([int(input()) for i in range(int(input()))],reverse=True)
for i in arr: print(i)