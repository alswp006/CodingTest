def solution(sizes):
    for i in range(len(sizes)):sizes[i]=sorted(sizes[i])
    answer =list(map(list,zip(*sizes)))
    return max(answer[0])*max(answer[1])