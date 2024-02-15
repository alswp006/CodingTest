n = int(input())

type = [64,32,16,8,4,2,1]
answer = 0

for i in type:
    if i <= n:
        n -= i
        answer+=1

print(answer)