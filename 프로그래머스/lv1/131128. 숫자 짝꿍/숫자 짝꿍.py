def solution(X, Y):
    answer = []
    x=[0]*10
    y=[0]*10
    for i in range(0,len(X)) : x[int(X[i])]+=1
    for i in range(0,len(Y)) : y[int(Y[i])]+=1
    for i in reversed(range(10)):
        if x[i]>0 and y[i]>0:
            if x[i]>y[i]:
                for j in range(0,y[i]):
                    answer.append(str(i))
            else :
                for j in range(0,x[i]):
                    answer.append(str(i))
    if len(answer)>0:
        if answer[0]=="0" : return "0"
    return "-1" if ''.join(answer)=="" else ''.join(answer)