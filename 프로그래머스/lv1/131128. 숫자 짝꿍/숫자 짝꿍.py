from collections import Counter
def solution(X, Y):
    answer = []
    x=Counter(X)
    y=Counter(Y)
    for i in reversed(range(10)):
        if str(i) in x and str(i) in y:
            for j in range(0,min(x[str(i)],y[str(i)])):answer.append(str(i))     
    if len(answer)>0:
        if answer[0]=="0" : return "0"
    return "-1" if ''.join(answer)=="" else ''.join(answer)