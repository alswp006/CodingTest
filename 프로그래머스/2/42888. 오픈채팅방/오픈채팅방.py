def solution(record):
    answer = []
    open_room = dict()
    
    for i in record:
        reco = i.split()
        if reco[0] == "Enter":
            open_room[reco[1]] = reco[2]
        elif reco[0] == "Change":
            open_room[reco[1]] = reco[2]
            
    for i in record:
        reco = i.split()
        if reco[0] == "Enter":
            answer.append(f"{open_room[reco[1]]}님이 들어왔습니다.")
        elif reco[0] == "Leave":
            answer.append(f"{open_room[reco[1]]}님이 나갔습니다.")
            
    return answer