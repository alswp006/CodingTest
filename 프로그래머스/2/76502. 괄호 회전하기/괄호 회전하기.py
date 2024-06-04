from collections import deque

def solution(s):
    answer = 0
    q = deque(s)
    for i in range(len(q)):
        n = len(q)
        flag = True
        stack=[]
        d = {"{" : "}", "[" : "]", "(" : ")"}
        while n != 0:
            if not flag:
                q.append(q.popleft())
                n -= 1
                continue
            x = q.popleft()
            if x in "({[":
                stack.append(x)
            else : 
                if len(stack) == 0 or d[stack.pop()] != x: 
                    flag = False
            
            q.append(x)
            n-=1
            
        if flag and len(stack) == 0:
            answer += 1

        q.append(q.popleft())
    
    return answer