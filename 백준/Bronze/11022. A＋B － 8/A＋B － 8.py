n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    print("Case #{0}: {1} + {2} = {3}".format(i+1,arr[i][0],arr[i][1],arr[i][0]+arr[i][1]))