import sys

input = sys.stdin.readline

n,m=map(int,input().split())
arr=set()
answer=[]
answer_num=0

for i in range(n):
    arr.add(str(input().rstrip()))

for i in range(m):
    s=str(input().rstrip())
    if s in arr:
        answer.append(s)
        answer_num+=1
answer.sort()
print(answer_num)
for i in answer:
    print(i)