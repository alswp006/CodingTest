arr=list(map(int,input().split()))
answer=[0 for i in range(len(arr))]
answer[0]=1-arr[0]
answer[1]=1-arr[1]
answer[2]=2-arr[2]
answer[3]=2-arr[3]
answer[4]=2-arr[4]
answer[5]=8-arr[5]
print(' '.join(map(str,answer)))