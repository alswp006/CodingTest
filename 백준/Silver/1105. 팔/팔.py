l,r = map(int,input().split())
ll, rr = str(l), str(r)
temp = 0
for i in range(len(ll)):
    if ll[i] != rr[i]:
        break
    if ll[i] == '8':
        temp += 1
print(temp if len(ll) == len(rr) else 0)