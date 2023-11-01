n,m = map(int,input().split())
arr = []
sum_num = [0,0]

for i in range(m):
    arr.append(int(input()))

arr.sort()

if n<m:
    arr=arr[m-n:]

for i in range(len(arr)):
    if (len(arr)-i) * arr[i] > sum_num[1]:
        sum_num[0] = arr[i]
        sum_num[1] = (len(arr)-i) * arr[i]

print(sum_num[0], end = ' ')
print(sum_num[1])