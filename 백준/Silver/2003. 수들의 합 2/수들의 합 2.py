import sys

input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

for i in range(len(arr)):
    temp = arr[i]
    if temp == m:
        answer+=1
        continue
    elif temp > m:
        continue
    for j in range(i+1, len(arr)):
        temp += arr[j]
        if temp > m:
            break
        elif temp == m:
            answer +=1
            break
print(answer)