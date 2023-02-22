n,m=map(int,input().split())
day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
wee=['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum=0
for i in range(n):
    sum+=day[i]
sum+=m
print(wee[sum%7])