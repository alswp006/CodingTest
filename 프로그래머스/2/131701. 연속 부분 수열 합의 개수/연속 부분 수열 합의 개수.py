from itertools import combinations

def solution(elements):
    answer = set()
    arr = elements * 2
    
    for i in range(len(elements)):
        answer.add(elements[i])
        for j in range(i + 1,i + len(elements) + 1):
            answer.add(sum(arr[i:j]))
    
    return len(answer)