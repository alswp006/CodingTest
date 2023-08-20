a,b,v=map(int,input().split())

m=v-a
n=a-b
answer=1
if m%n==0:
    answer+=m//n
else:
    answer+=m//n+1
print(answer)