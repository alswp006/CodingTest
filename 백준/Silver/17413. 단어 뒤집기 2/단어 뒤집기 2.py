def reverse_print(temp):
    for i in range(len(temp)-1,-1,-1):
        print(temp[i],end='')

s = input()
temp = []
check = 0

for i in s:
    if check == 0:
        if i == '<' :
            check += 1
            reverse_print(temp)
            print('<',end='')
            temp=[]
        elif i == ' ':
            reverse_print(temp)
            print(' ',end='')
            temp=[]
        else:
            temp.append(i)
    else:
        if i == '>':
            print('>',end='')
            check-=1
        else:
            print(i,end='')

reverse_print(temp)