def solution(number, limit, power):
    answer = 1
    for i in range(2,number+1):
        a=2
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                if i/j==j: a+=1
                else: a+=2
            if a>limit:
                a=power
                break
        answer+=a
    return answer