a,b,v=map(int,input().split())
m=v-a
n=a-b
print(m//n+1 if m%n==0 else m//n+2)