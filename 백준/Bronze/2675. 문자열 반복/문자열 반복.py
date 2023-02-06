n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(str,input().split())))
for i in range(n):
    answer=[]
    arr[i][0]=int(arr[i][0])
    for j in arr[i][1]:
        answer.append(j*arr[i][0])
    print(''.join(answer))