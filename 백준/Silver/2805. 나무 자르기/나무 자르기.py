import sys

# 입력을 더 빠르게 받기 위해 sys.stdin.readline 사용
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
# 나무 높이를 내림차순으로 정렬
heights = sorted(list(map(int, input().split())), reverse=True)
# 이진 탐색을 위한 시작점과 끝점 설정
low, high = 1, sum(heights)

# 이진 탐색 수행
while low <= high:
    mid = (low + high) // 2
    count = 0

    # 현재 설정된 높이(mid)보다 큰 나무들에 대해 잘라낼 수 있는 양 계산
    for height in heights:
        if height > mid:
            count += height - mid
    # 필요한 양 이상으로 자를 수 있는 경우, 더 높은 높이 탐색
    if count >= m:
        low = mid + 1
    else:
        high = mid - 1

# 가능한 최대 높이 출력
print(high)
