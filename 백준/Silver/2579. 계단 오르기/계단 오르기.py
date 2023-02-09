n=int(input())
answer=[0]*301
arr=[0]
for _ in range(n):
    arr.append(int(input()))
if len(arr)==2:answer[1]=arr[1]
elif len(arr)==3:answer[2]=arr[1]+arr[2]
else:
    answer[1]=arr[1]
    answer[2]=answer[1]+arr[2]
    answer[3]=max(arr[1]+arr[3],arr[2]+arr[3])
    for i in range(4,n+1):
        answer[i]=max(answer[i-3]+arr[i-1]+arr[i],answer[i-2]+arr[i])
print(answer[n])