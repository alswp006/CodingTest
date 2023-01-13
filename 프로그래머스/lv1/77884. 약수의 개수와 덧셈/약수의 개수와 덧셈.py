def solution(left, right):
    answer=[i for i in range(left,right+1) if i**.5-int(i**.5)==0]
    return sum([i for i in range(left,right+1) if i**.5-int(i**.5)!=0])-sum(answer)