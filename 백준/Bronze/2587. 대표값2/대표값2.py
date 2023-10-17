answer=0
arr=[]
for i in range(5):
    n=int(input())
    answer+=n
    arr.append(n)
arr.sort()
print(answer//5)
print(arr[2])