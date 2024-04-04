n = int(input())
moves = [[n, 1, 3]]
print(2 ** n - 1)

while moves:
    n, start, end = moves.pop()
    if n == 1:
        print(start, end)
        continue
    # 세 번째 단계: n-1 개를 보조 기둥에서 목표 기둥으로 이동
    moves.append((n - 1, 6 - start - end, end))
    # 두 번째 단계: 가장 큰 원판을 시작 기둥에서 목표 기둥으로 이동
    moves.append((1, start, end))
    # 첫 번째 단계: n-1 개를 시작 기둥에서 보조 기둥으로 이동
    moves.append((n - 1, start, 6 - start - end))
