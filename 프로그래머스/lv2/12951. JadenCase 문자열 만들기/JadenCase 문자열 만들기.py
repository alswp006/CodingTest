def solution(s):
    s=s.split(' ')
    answer = [s[i].capitalize() for i in range(len(s))]
    return ' '.join(answer)