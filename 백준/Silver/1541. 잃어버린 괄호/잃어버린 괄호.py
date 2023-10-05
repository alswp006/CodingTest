arr=list(map(str,input().split('-')))
temp = sum(map(int,arr[0].split('+')))
for i in range(1,len(arr)):
    temp-=sum(map(int,arr[i].split('+')))
print(temp)