import sys

print(''.join(map(str,sorted(list(map(int,sys.stdin.readline().rstrip())),reverse=True))))