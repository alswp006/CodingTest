import sys
input=sys.stdin.readline
arr=[0]
answer=0
for i in range(int(input())):
    arr.append(int(input()))
arr.sort()
for i in range(len(arr)):
    answer+=abs(i-arr[i])
print(answer)