s=list(map(int,input()))
count=[0,0]
prev=s[0]
count[prev]+=1
for i in range(1,len(s)):
    now=s[i]
    if prev != now:
        count[now]+=1
    prev=now
print(min(count))