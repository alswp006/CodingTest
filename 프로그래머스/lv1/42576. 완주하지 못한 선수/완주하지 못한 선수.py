def solution(participant, completion):
    participant.sort() 
    completion.sort()
    for i in range(len(completion)):
        if participant[i]!=completion[i]:return ''.join(participant[i])
    return ''.join(participant[i+1])
