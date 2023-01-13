def solution(numbers):
    s = set([i for i in range(0,10)])
    return sum(s-set(numbers))