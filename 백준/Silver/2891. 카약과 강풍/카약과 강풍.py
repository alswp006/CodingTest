t,s,r=map(int,input().split())
st = list(map(int,input().split()))
rt = list(map(int,input().split()))
removest=[]
for i in st:
    if i in rt:
        removest.append(i)
        rt.remove(i)
        s-=1
for i in removest:
    st.remove(i)
for i in st:
    if i-1 in rt:
        rt.remove(i-1)
        s-=1
    elif i+1 in rt:
        rt.remove(i+1)
        s-=1
print(s)