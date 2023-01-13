def solution(a, b):
    return sum([i for i in range(a,b+1)]) if b>a else sum([i for i in range(b,a+1)])