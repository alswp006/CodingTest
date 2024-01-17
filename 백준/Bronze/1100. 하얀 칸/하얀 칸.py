import sys

input = sys.stdin.readline

arr = [list(input().rstrip()) for i in range(8)]
answer = 0

for i in range(8):
    for j in range(8):
        if i % 2 == 0 :
            if j % 2 == 0:
                if arr[i][j] == 'F':
                    answer+=1
                    continue
            continue
        if j % 2 == 1:
            if arr[i][j] == 'F':
                answer+=1
print(answer)