def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(x,y):
    return x*y//gcd(x,y)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    print(lcm(arr[i][0],arr[i][1]))