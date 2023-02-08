from collections import Counter
answer=[]
s=dict(Counter(list(input().upper())))
for k,v in s.items():
    if v==max(s.values()):
        answer.append(k)
if len(answer)>1:print("?")
else: print(''.join(answer))