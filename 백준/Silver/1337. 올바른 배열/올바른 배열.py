import sys

input = sys.stdin.readline
arr = sorted(int(input()) for i in range(int(input())))
answer = 10**9

for i in arr:
    count = 0
    for j in range(i,i+5):
        if j not in arr:
            count+=1
    answer = min(answer,count)
print(answer)