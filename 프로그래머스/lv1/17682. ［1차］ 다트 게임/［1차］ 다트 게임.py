def solution(dartResult):
    answer = []
    for i in range(len(dartResult)):
        if dartResult[i].isdecimal():
            if dartResult[i-1]=='1' and dartResult[i]=='0':continue
            if dartResult[i+1].isdecimal():
                answer.append(int(dartResult[i:i+2]))
            else:
                answer.append(int(dartResult[i]))
            print(answer)
        else:
            if dartResult[i]=='D':
                answer[-1]=answer[-1]**2
            if dartResult[i]=='T':
                answer[-1]=answer[-1]**3
            if dartResult[i]=='*':
                if i==2:
                    answer[-1]*=2
                else:
                    answer[-1]*=2
                    answer[-2]*=2
            if dartResult[i]=='#':
                answer[-1]*=-1
    return sum(answer)