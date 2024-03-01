import sys

input = sys.stdin.readline

answer=[]

arr = [0] + [int(input()) for i in range(int(input()))]

for i in range(1,len(arr)):
    if i in answer:
        continue

    temp = set()
    temp_index = set()
    index = i

    while True:
        if arr[index] < len(arr):
            if arr[index] not in temp:
                temp.add(arr[index])
                temp_index.add(index)
                index = arr[index]
            else:
                if temp == temp_index:
                    for i in temp:
                        answer.append(i)
                break
        else:
            break
print(len(answer))
for i in sorted(answer):
    print(i)