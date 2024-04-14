import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int,input().split())
    team = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    count_submit = [0 for _ in range(n + 1)]
    team_total_score = [0 for _ in range(n + 1)]
    last_submit = [0 for _ in range(n + 1)]
    answer = 1

    for i in range(m):
        team_id, question, score = map(int,input().split())
        if team[team_id][question] < score:
            team_total_score[team_id] += score - team[team_id][question]
            team[team_id][question] = score
        count_submit[team_id] += 1
        last_submit[team_id] = i

    my_team_score = team_total_score[t]
    for i in range(1, n + 1):
        if team_total_score[i] > my_team_score:
            answer += 1
        elif team_total_score[i] == my_team_score:
            if count_submit[i] < count_submit[t]:
                answer += 1
            elif count_submit[i] == count_submit[t]:
                if last_submit[i] < last_submit[t]:
                    answer += 1
    print(answer)
