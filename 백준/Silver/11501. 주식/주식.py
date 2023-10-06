import sys

input=sys.stdin.readline

def max_find():
    while index_arr[-1]==0:
        index_arr.pop()
        if len(arr) == 0: break
    return len(index_arr)-1

for _ in range(int(input())):
    answer = 0
    index_arr = [0] * 10001
    n=int(input())
    arr=list(map(int,input().split()))
    for i in arr:
        index_arr[i]+=1
    max = max_find()
    for i in range(0,len(arr)-1):
        index_arr[arr[i]] -= 1
        if max == arr[i]:
            max = max_find()
        else:
            answer+=max-arr[i]
    print(answer)