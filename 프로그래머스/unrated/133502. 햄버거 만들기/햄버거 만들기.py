def solution(ingredient):
    answer=0
    i=0
    while i<len(ingredient)-3:
        if ingredient[i]!=1:
            i+=1
            continue
        if ingredient[i+1:i+4]==[2,3,1]:
            del ingredient[i:i+4]
            answer+=1
            if i>0:i=i-2
            continue
        i+=1
    return answer