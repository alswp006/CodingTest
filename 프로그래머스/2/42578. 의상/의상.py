from math import prod

def solution(clothes):
    d = dict()
    for i in clothes:
        if i[1] in d : d[i[1]]+= 1
        else : d[i[1]] = 2
    
    return prod(i for i in d.values()) - 1