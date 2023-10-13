answer=[]
s=input()
temp=0

def string_input(temp):
    if temp % 2 == 0:
        answer.append('AAAA' * (temp // 4))
        temp %= 4
        answer.append('BB' * (temp // 2))
        temp %= 2
    else:
        print(-1)
        exit()

for i in range(len(s)):
    if s[i] == 'X':
        temp+=1
        if len(s)-1 != i:
            if s[i+1] == '.':
                string_input(temp)
                temp=0
        else:
            string_input(temp)
            temp=0
    else:
        answer.append('.')
print(''.join(answer))