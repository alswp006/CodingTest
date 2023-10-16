import sys

num_count=[0] * 8002
sum_num=0
arr=[]

n=int(input())
for i in range(n):
    num=int(sys.stdin.readline())
    num_count[num+4000]+=1
    sum_num+=num
    arr.append(num)
arr.sort()
print(round(sum_num/n))
print(arr[n//2])
ma=max(num_count)
if num_count.count(ma)>1:
    count=0
    for i in range(len(num_count)):
        if num_count[i] == ma:
            count+=1
            if count==2:
                print(i-4000)
                break
else:
    ma_index = num_count.index(ma)
    print(ma_index-4000)
print(arr[-1]-arr[0])