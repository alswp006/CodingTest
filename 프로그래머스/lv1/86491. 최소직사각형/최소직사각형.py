def solution(sizes):
    ma=max(sizes[0])
    mi=min(sizes[0])
    for i in sizes:
        ma=max(ma,max(i))
        mi=max(mi,min(i))
    return ma*mi