n = int(input())
nums = list(map(int,input().split()))
target = int(input())
answer = 0
nums.sort()
start, end = 0, n - 1

while start < end :
    num_sum = nums[start] + nums[end]
    if  num_sum == target :
        start += 1
        end -= 1
        answer += 1
    elif num_sum < target : start += 1
    else : end -= 1

print(answer)