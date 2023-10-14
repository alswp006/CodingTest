import sys
input = sys.stdin.readline

arr=[int(input()) for i in range(int(input()))]
print('\n'.join(map(str,sorted(arr,reverse=True))))