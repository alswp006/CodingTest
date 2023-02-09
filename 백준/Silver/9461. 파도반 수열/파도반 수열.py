answer=[]
for _ in range(int(input())):
    n=int(input())
    arr=[0,1,1,1,2,2]
    for i in range(6,n+1):
        arr.append(arr[i-1]+arr[i-5])
    answer.append(arr[n])
for i in answer:print(i)