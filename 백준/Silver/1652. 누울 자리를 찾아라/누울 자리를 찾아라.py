n=int(input())
arr=[]
answer=[0,0]
a=0
for i in range(n):
    inpp=list(map(str,input()))
    arr.append(inpp)
    for j in range(len(inpp)-1):
        if inpp[j]=='.' and inpp[j+1]=='.' and a==0:
            answer[0]+=1
            a=1
        if inpp[j]=='X':a=0
    a=0
for i in range(n):
    for j in range(n-1):
        if arr[j][i]=='.' and arr[j+1][i]=='.' and a==0:
            answer[1]+=1
            a=1
        if arr[j][i]=='X':a=0
    a=0
print(answer[0],end=' ')
print(answer[1])