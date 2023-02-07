n=int(input())
num1,num2=100,100
for i in range(n):
    x,y=map(int,input().split())
    if x>y:num2-=x
    elif x<y:num1-=y
print(num1)
print(num2)