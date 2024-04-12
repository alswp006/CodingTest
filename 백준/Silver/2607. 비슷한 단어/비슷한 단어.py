import sys

input = sys.stdin.readline

n = int(input())
ans_word = input().rstrip()
ans_word_cnt = [0] * 26
for i in ans_word: ans_word_cnt[ord(i) - 65] += 1
answer = 0

for i in range(n - 1):
    word_cnt = ans_word_cnt.copy()
    for w in input().rstrip():
        word_cnt[ord(w) - 65] -= 1
    one_cnt = word_cnt.count(1)
    minus_one_cnt = word_cnt.count(-1)
    zero_cnt = word_cnt.count(0)
    if zero_cnt == 26: # 단어가 모두 일치할 때
        answer+=1
    elif  one_cnt == 1 and  minus_one_cnt == 1 and zero_cnt == 24: # 단어 한 개를 바꾸면 될 때
        answer += 1
    elif one_cnt == 1 and minus_one_cnt == 0 and zero_cnt == 25: # 단어 한 개를 빼면 될 때
        answer += 1
    elif one_cnt == 0 and minus_one_cnt == 1 and zero_cnt == 25: # 단어 한 개를 더하면 될 때
        answer += 1

print(answer)

