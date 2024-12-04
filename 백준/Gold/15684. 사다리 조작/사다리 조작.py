import sys

def main():
    N, M, H = map(int, sys.stdin.readline().split())
    ladder = [[0] * N for _ in range(H)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        ladder[a - 1][b - 1] = 1

    def is_valid_ladder():
        for start in range(N):
            position = start
            for level in range(H):
                if ladder[level][position]:
                    position += 1
                elif position > 0 and ladder[level][position - 1]:
                    position -= 1
            if position != start:
                return False
        return True

    def dfs(count, x, y):
        nonlocal min_count
        if count >= min_count:
            return
        if is_valid_ladder():
            min_count = count
            return
        if count == 3:
            return
        for i in range(x, H):
            start_j = y if i == x else 0
            for j in range(start_j, N - 1):
                if ladder[i][j]:
                    continue
                if j > 0 and ladder[i][j - 1]:
                    continue
                if j < N - 2 and ladder[i][j + 1]:
                    continue
                ladder[i][j] = 1
                dfs(count + 1, i, j + 2)
                ladder[i][j] = 0

    min_count = 4
    dfs(0, 0, 0)
    print(-1 if min_count > 3 else min_count)

if __name__ == "__main__":
    main()