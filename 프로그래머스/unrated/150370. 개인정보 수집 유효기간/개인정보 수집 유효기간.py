def solution(today, terms, privacies):
    answer = []
    terms_dic = {term.split(' ')[0] : int(term.split(' ')[1])*28 for term in terms}
    t_y, t_m, t_d = today.split('.')
    today = int(t_y)*12*28 + int(t_m)*28 + int(t_d)
    
    for idx, p in enumerate(privacies):
        year,month,day = p.split('.')
        day,term = day.split(' ')
        check_day = int(year)*12*28 + int(month)*28 + int(day)
        
        if check_day+terms_dic[term] <= today:
            answer.append(idx+1)
    
    return answer