n,m=map(int,input().split())
arr=[]
answer=0
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x :(-x[1],-x[2],-x[3]))
for i in arr:
    if i[0]==m:
        a,b,c=i[1],i[2],i[3]
for i in range(len(arr)):
    if arr[i][1]==a and arr[i][2]==b and arr[i][3]==c:
        answer=i
        break
print(answer+1)