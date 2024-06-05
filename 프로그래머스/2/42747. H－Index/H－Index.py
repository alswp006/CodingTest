def solution(citations):
    answer = len(citations)
    citations.sort()
    
    for i in citations:
        if i < answer:
            answer -= 1
        
    return answer