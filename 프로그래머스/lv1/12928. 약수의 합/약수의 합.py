def solution(n):
    return n+sum(list(filter(lambda x:n%x==0,range(1,(n//2)+1))))