from itertools import permutations
def solution(numbers):
    arr=[]
    for i in range(1,len(numbers)+1):
        num=permutations(numbers,i)
        num=list(num)
        for i in num:arr.append(int(''.join(i)))
    arr=list(set(arr))
    if 0 in arr:arr.remove(0)
    if 1 in arr:arr.remove(1)
    answer=len(arr)
    for i in arr:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                answer-=1
                break
    return answer