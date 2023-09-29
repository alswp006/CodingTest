s = input()
answer = []

for i in s:
    ascii_c = ord(i)
    if ascii_c >= 65 and ascii_c <= 90:
        ascii_c += 13
        if ascii_c >= 91:
            ascii_c -= 26
        answer.append(chr(ascii_c))
    elif ascii_c >= 97 and ascii_c <= 122:
        ascii_c +=13
        if ascii_c >= 123:
            ascii_c-=26
        answer.append(chr(ascii_c))
    else:
        answer.append(i)
print(''.join(answer))