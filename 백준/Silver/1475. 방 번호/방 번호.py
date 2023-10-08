import sys

arr=[0]*10
n=sys.stdin.readline().rstrip()

for i in n:
    arr[int(i)]+=1
if (arr[6]+arr[9])%2==0:
    arr[6]=(arr[6]+arr[9])//2
    arr[9] = 0
else:
    arr[6] = (arr[6] + arr[9]) // 2
    arr[9] = arr[6] + 1
print(max(arr))