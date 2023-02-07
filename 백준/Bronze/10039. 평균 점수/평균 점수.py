answer=0
for i in range(5):
    a=int(input())
    if a<=40: answer+=40
    else:answer+=a
print(int(answer/5))