n = int(input())
x,y = 0,1

for i in range(2,n+1):
    x, y = y, (x+y)%1000000007

print(y if n != 0 else x)