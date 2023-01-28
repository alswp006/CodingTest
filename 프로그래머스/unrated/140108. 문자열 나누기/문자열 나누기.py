def solution(s):
    answer = 1
    a=s[0]
    x,y=1,0
    for i in range(1,len(s)-1):
        if s[i]==a:
            x+=1
        else :
            y+=1
        if x==y:
            answer+=1
            x,y=0,0
            a=s[i+1]
            
    return answer