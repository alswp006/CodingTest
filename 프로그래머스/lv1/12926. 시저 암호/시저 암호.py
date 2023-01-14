def solution(s, n):
    answer = []
    s=list(s)
    for i in s:
        if i == " ":
            answer.append(" ")
            continue
        if ord(i)>=66 and ord(i)<=90: 
            if ord(i)+n>90:
                answer.append(chr(ord(i)+n-26))
                continue
            else:
                answer.append(chr(ord(i)+n))
        else:
            if ord(i)+n>122:
                answer.append(chr(ord(i)+n-26))
                continue
            else:
                answer.append(chr(ord(i)+n))
    return ''.join(answer)