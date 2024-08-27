s = input()
arr = []
answer = 0
temp_R = 0
left_K = 0
r_cnt = 0
k = s.count('K')
flag = False
for i in range(len(s)):
    if s[i] == "R" and not flag:
        flag = True
        temp_R = i
    elif s[i] == "K" and flag:
        flag = False
        arr.append([left_K, i - temp_R])
        r_cnt += i - temp_R
        left_K += 1
    elif s[i] == "K": left_K += 1
else:
    if s[-1] == "R":
        arr.append([k, len(s) - temp_R])
        r_cnt += len(s) - temp_R

l,r = 0, len(arr) - 1

while l <= r:
    answer = max(answer, r_cnt + min(arr[l][0], k - arr[r][0]) * 2)
    if arr[l][0] < k - arr[r][0]:
        r_cnt -= arr[l][1]
        l += 1
    elif arr[l][0] > k - arr[r][0]:
        r_cnt -= arr[r][1]
        r -= 1
    else:
        r_cnt -= arr[l][1] + arr[r][1]
        l += 1
        r -= 1

print(answer)
