import sys
arr = sorted([list(map(str,input().split())) for i in range(int(sys.stdin.readline()))], key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in arr:print(i[0])