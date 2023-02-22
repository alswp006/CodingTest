import sys
input=sys.stdin.readline
arr=[]
answer=[]
for i in range(int(input())):
    arr.append(list(map(int,input().split())))
    answer.append([0 for i in range(3)])
answer[0]=arr[0]
for i in range(1,len(answer)):
    for j in range(3):
        if j==0:
            answer[i][j]=min(answer[i-1][j+1],answer[i-1][j+2])+arr[i][j]
        elif j==1:
            answer[i][j]=min(answer[i-1][j-1],answer[i-1][j+1])+arr[i][j]
        elif j==2:
            answer[i][j]=min(answer[i-1][j-2],answer[i-1][j-1])+arr[i][j]
print(min(answer[-1]))