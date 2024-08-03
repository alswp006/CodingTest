import sys

def count_installations(distance):
    count = 1
    last = houses[0]
    for house in houses:
        if house >= last + distance:
            count += 1
            if count >= c:
                return True
            last = house
    return False

input = sys.stdin.readline
n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))
result = 0
start, end = 1, houses[-1] - houses[0]

while start <= end:
    mid = (start + end) // 2
    if count_installations(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)