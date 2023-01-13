def solution(x, n):
    return [x+x*i for i in range(0,n)] if x!=0 else [x for i in range(0,n)]