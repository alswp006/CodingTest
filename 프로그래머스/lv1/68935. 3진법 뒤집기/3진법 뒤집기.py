def solution(n):
    answer = ''
    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)
    return int(answer,3)
