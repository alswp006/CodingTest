import sys

N, L = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0


def is_valid_path(line):
    ramp_used = [False] * N
    for i in range(1, N):
        height_diff = line[i] - line[i - 1]
        if abs(height_diff) > 1:
            return False
        elif height_diff == 1:
            for j in range(L):
                idx = i - 1 - j
                if idx < 0 or line[idx] != line[i - 1] or ramp_used[idx]:
                    return False
                ramp_used[idx] = True
        elif height_diff == -1:
            for j in range(L):
                idx = i + j
                if idx >= N or line[idx] != line[i] or ramp_used[idx]:
                    return False
                ramp_used[idx] = True
    return True


for row in grid:
    if is_valid_path(row):
        answer += 1
for col in zip(*grid):
    if is_valid_path(col):
        answer += 1

print(answer)
