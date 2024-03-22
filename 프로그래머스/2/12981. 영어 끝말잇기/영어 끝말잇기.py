from collections import deque
def solution(n, words):
    s = set()
    s.add(words[0])
    d = 0
    
    for i in range(1, len(words)):
        if words[i] in s:
            d = i
            break
        if words[i-1][-1] != words[i][0]:
            d = i
            break
        s.add(words[i])
    else:
        return [0,0]
        
    return [i % n + 1, i // n + 1]