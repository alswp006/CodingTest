str=''
while True:
    answer=0
    str=input()
    if str=='#':break
    for i in str:
        if i == 'a' or i == 'A':answer+=1
        elif i == 'e' or i == 'E': answer += 1
        elif i == 'i' or i == 'I': answer += 1
        elif i == 'o' or i == 'O': answer += 1
        elif i == 'u' or i == 'U': answer += 1
    print(answer)