def solution(t, p):
    answer=0
    arr=[t[i:i+len(p)] for i in range(0,len(t)-len(p)+1)]
    print(arr)
    for i in arr:
        if i<=p:answer+=1
    return answer