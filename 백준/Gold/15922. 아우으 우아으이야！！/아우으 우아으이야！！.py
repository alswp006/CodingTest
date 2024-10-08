import sys

n = int(input())
left, right = map(int, input().split())
empty = 0

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    if right < x:
        empty += x - right
    right = y if y > right else right

print(right - left - empty)