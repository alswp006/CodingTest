def solution(topping):
    answer = 0
    a = dict()
    b = set()
    
    for i in topping:
        if i not in a:
            a[i] = 1
            continue
        a[i] += 1
        
    for i in topping:
        a[i] -= 1
        if a[i] == 0:
            del (a[i])
        
        b.add(i)
        
        if len(a) == len(b):
            answer += 1
        
    return answer