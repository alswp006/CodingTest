def solution(m, musicinfos):
    answer = ''
    d = dict()
    for i in musicinfos:
        start_time, end_time, name, code = map(str, i.split(","))
        start_hours, start_minute = map(int, start_time.split(":"))
        end_hours, end_minute = map(int, end_time.split(":"))
        time = (end_hours - start_hours) * 60 + (end_minute - start_minute)
        temp = ''
        limit = 0
        point = 0
        while limit != time:
            temp_a = code[point % len(code)]
            point += 1
            if temp_a != "#":
                limit += 1
            temp += temp_a
        else:
            if code[point % len(code)] == "#": temp += "#"
        d[name] = temp
    arr = sorted(d.items(), key = lambda x : -len(x[1].replace("#", "")))
    
    for name, code in arr:
        temp_len = len(code)
        point = 0
        for i in range(temp_len):
            if temp_len < i + len(m):break
            if code[i:i + len(m)] != m: continue
            if temp_len == i + len(m) : return name
            if code[i + len(m)] != "#" : return name
    return "(None)"