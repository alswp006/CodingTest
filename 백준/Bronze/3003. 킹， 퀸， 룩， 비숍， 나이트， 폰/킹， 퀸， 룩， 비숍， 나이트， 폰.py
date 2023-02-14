arr=list(map(int,input().split()))
answer=[0 for i in range(len(arr))]
c=[1,1,2,2,2,8]
for i in range(6):
    answer[i]=c[i]-arr[i]
print(' '.join(map(str,answer)))