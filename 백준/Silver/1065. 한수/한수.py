num = int(input())

answer = 0
for i in range(1, num+1):
    if i < 100:
        answer += 1
        continue
    if (i // 10 % 10) - (i % 10) == (i // 100) - (i // 10 % 10):
        answer += 1 
print(answer)