def solution(t, p):
    arr=[t[i:i+len(p)] for i in range(0,len(t)-len(p)+1)]
    return sum([1 for i in arr if i<=p])