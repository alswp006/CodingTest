def solution(id_list, report, k):
    report=list(set(report))
    user_num={}
    report_send={}
    report_receive={}
    for i in id_list:
        report_send[i]=[]
        report_receive[i]=0
        user_num[i]=0
    for i in range(len(report)):report[i]= report[i].split(" ")
    for i in range(len(report)):
        report_send[report[i][0]].append(report[i][1])
        report_receive[report[i][1]]+=1
        if report_receive[report[i][1]]>=k:continue
    for user,rep in report_receive.items():
        if rep>=k:
            for userid,reuser in report_send.items():
                if user in reuser:user_num[userid]+=1
    return [i for i in user_num.values()]