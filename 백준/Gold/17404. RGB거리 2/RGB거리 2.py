INF = float('inf')

def main():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    min_total_cost = INF

    RED, GREEN, BLUE = 0, 1, 2

    for first_color in (RED, GREEN, BLUE):
        dp = [[INF] * 3 for _ in range(n)]
        dp[0][first_color] = costs[0][first_color]

        for house in range(1, n):
            dp[house][RED] = costs[house][RED] + min(dp[house - 1][GREEN], dp[house - 1][BLUE])
            dp[house][GREEN] = costs[house][GREEN] + min(dp[house - 1][RED], dp[house - 1][BLUE])
            dp[house][BLUE] = costs[house][BLUE] + min(dp[house - 1][RED], dp[house - 1][GREEN])

        for last_color in (RED, GREEN, BLUE):
            if last_color != first_color:
                min_total_cost = min(min_total_cost, dp[-1][last_color])

    print(min_total_cost)

if __name__ == "__main__":
    main()