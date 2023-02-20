from itertools import product
def solution(num,n):
    l=[(x,-x)for x in num]
    s=list(map(sum,product(*l)))
    return s.count(n)