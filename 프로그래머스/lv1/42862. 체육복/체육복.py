def solution(n, lost, reserve):
    l=n-len(lost)
    lost=sorted(lost)
    reserve=sorted(reserve)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            l+=1
            continue
        elif i-1 in reserve and not i-1 in lost:
            reserve.remove(i-1)
            l+=1
            continue
        elif i+1 in reserve and not i+1 in lost:
            reserve.remove(i+1)
            l+=1
            continue
    return l