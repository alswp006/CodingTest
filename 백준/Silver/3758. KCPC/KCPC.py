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
    my_team_count = count_submit[t]
    my_team_last = last_submit[t]

    for i in range(1, n + 1):
        if (team_total_score[i] > my_team_score) or \
            (team_total_score[i] == my_team_score and count_submit[i] < my_team_count) or \
            (team_total_score[i] == my_team_score and count_submit[i] == my_team_count and last_submit[i] < my_team_last):
            answer += 1
    print(answer)
