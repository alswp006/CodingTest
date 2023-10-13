import sys

input = sys.stdin.readline
arr=[]
answer=0

for i in range(int(input())):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    temp = arr[i] - i
    if temp>0:
        answer+=temp
print(answer)