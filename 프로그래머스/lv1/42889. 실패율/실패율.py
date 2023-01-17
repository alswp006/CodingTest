def solution(N, stages):
    d={}
    l=len(stages)
    for i in range(1,N+1):
        if l==0:d[i]=stages.count(i)/1
        else:d[i]=stages.count(i)/l
        l-=stages.count(i)
        
    answer=sorted(d.items(),key=lambda x:x[1],reverse=True)
    return [answer[i][0] for i in range(len(answer))]