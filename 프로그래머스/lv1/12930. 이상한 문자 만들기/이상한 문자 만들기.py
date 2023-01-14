def solution(s):
    s=list(s.upper())
    n=0
    for i in range(len(s)):
        if n%2!=0:
            s[i]=s[i].lower()
            n+=1
        else : n+=1
        if s[i]==" ":
            n=0
    return ''.join(s)
        