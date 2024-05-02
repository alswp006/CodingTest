import sys
from collections import deque
from itertools import combinations
import math
input = sys.stdin.readline

n, k = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(n)]


def find_chicken_house():
    chicken = []
    for i in range(n):
        for j in range(n):
            if town[i][j] == 2:
                chicken.append([i, j])
    return chicken


def distance_cal(chicken_house):
    sep_distance = []
    for i, j in chicken_house:
        distance = [[251 for _ in range(n)] for _ in range(n)]
        distance[i][j] = 0
        q = deque([[i, j]])
        move_type = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            x, y = q.popleft()
            for dx, dy in move_type:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if distance[nx][ny] != 251:
                    continue
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])

        final_distance = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if town[x][y] == 1:
                    final_distance[x][y] = distance[x][y]

        sep_distance.append(final_distance)
    return sep_distance

def find_min_distance():
    temp = [i for i in range(len(chicken_house))]
    chicken_comb = list(combinations(temp, k))
    sum_distance = [0 for i in range(len(chicken_comb))]

    for x in range(n):
        for y in range(n):
            if town[x][y] == 1:
                for i in range(len(chicken_comb)):
                    num = 251
                    for j in chicken_comb[i]:
                        num = min(num, sep_distance[j][x][y])
                    sum_distance[i] += num
    return min(sum_distance)


chicken_house = find_chicken_house()
sep_distance = distance_cal(chicken_house)
print(find_min_distance())