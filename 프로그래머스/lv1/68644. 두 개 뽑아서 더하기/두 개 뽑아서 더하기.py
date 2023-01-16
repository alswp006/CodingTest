def solution(numbers):
    from itertools import combinations
    return sorted(list(set([sum(i) for i in combinations(numbers,2) ])))