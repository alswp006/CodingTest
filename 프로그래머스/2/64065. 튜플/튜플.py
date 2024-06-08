def solution(s):
    arr=[]
    answer=[]
    dupl_check=set()
    temp = s.replace("{","").replace("},", "/").replace("}","").split("/")
    
    for i in temp:
        arr.append(i.split(","))
        
    arr.sort(key = len)
    
    
    for i in arr:
        for j in i:
            if j not in dupl_check:
                answer.append(int(j))
                dupl_check.add(j)
    return answer