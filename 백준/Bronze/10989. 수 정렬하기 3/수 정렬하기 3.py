import sys
input = sys.stdin.readline
answer=[0 for _ in range(10001)]
for i in range(int(input())):
    answer[int(input())]+=1
for i in range(len(answer)):
    for j in range(1,answer[i]+1):
        sys.stdout.write(str(i)+'\n')