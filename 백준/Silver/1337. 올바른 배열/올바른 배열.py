import sys

input = sys.stdin.readline
arr = sorted(int(input()) for i in range(int(input())))
answer = 4

for i in arr:
    count = 4
    for j in range(i+1,i+5):
        if j in arr:
            count-=1
    answer = min(answer,count)
print(answer)