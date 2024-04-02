import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# 이진 탐색을 위한 시작점과 끝점 설정
start, end = 1, max(arr)

# 이진 탐색 알고리즘으로 적절한 랜선 길이 찾기
while start <= end:
    mid = (start + end) // 2  # 중간 길이 값

    # 현재의 mid 길이로 만들 수 있는 랜선 개수 계산
    num_cables_made = sum(cable_length // mid for cable_length in arr)

    # 만들 수 있는 랜선의 개수가 필요한 개수보다 부족하면, 더 짧은 길이를 탐색
    if num_cables_made < m:
        end = mid - 1
    # 만들 수 있는 랜선의 개수가 필요한 개수보다 많거나 같으면, 더 긴 길이도 가능한지 확인
    else:
        start = mid + 1

# 가능한 최대 랜선 길이 출력 (end 출력)
print(end)

