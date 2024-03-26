n, m = map(int, input().split())

def solution(n, k):
    cnt = 0
    while n > 1:
        n //= k
        cnt += n

    return cnt

two = solution(n, 2) - solution(m, 2) - solution(n - m, 2)
five = solution(n, 5) - solution(m, 5) - solution(n - m, 5)

print(min(two, five))