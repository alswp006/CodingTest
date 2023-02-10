import sys
input = sys.stdin.readline
answer=[]
for i in range(int(input())):
    answer.append(int(input()))
answer.sort()
for i in answer:
    sys.stdout.write(str(i)+'\n')