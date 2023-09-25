a = int(input())
b = int(input())
answer=a*b

for i in range(3):
    answer_1=a*(b%10)
    print(answer_1)
    b=b//10
print(answer)