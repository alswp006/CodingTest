def solution(a, b, n):
    answer=0
    while n>a-1:
        answer+=(n//a)*b
        nn=n%a
        n=(n//a)*b+nn
    return answer