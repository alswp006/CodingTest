def solution(nums):
    from itertools import combinations
    arr=list([sum(i) for i in combinations(nums,3)])
    answer = len(arr)
    print(arr)
    for i in arr:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                answer-=1
                break
    return answer