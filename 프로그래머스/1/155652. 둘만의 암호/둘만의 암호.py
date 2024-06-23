def solution(s, skip, index):
    answer = []
    alphabet = []
    skip_num = set([ord(i) for i in skip])
    for i in range(97, 123):
        if i not in skip_num:
            alphabet.append(chr(i))
    
    for i in s:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                answer.append(alphabet[(j + index) % len(alphabet)])

    return ''.join(answer)