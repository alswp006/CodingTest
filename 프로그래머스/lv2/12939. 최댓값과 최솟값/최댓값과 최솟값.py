def solution(s):
    s=list(map(int,s.split(' ')))
    arr=[min(s),max(s)]
    return ' '.join(map(str,arr))