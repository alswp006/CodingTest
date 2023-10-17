n=int(input())
arr=list(map(int,input().split()))
k=int(input())
answer=[0,0]
arr.sort()
for i in range(len(arr)):
    if k<arr[i]:
        if i == 0:
            answer[1]=arr[i]
        else:
            answer[0]=arr[i-1]
            answer[1]=arr[i]
        break
    elif k==arr[i]:
        print(0)
        exit()
print((k-answer[0]-1)*(answer[1]-k)+answer[1]-(k+1))