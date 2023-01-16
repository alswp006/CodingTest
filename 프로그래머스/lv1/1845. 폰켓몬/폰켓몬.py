def solution(nums):
    s = set(nums)
    answer = 0
    return len(nums)//2 if len(s)>len(nums)//2 else len(s)