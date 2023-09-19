answer=0
num_list=[0 for _ in range(10)]
color_equal=0
number_continue=0
num_max=0
temp_color="a"

for i in range(5):
    a,b=map(str,input().split())
    if temp_color==a:
        color_equal+=1
    temp_color=a
    b=int(b)
    num_list[b]+=1
    num_max=max(num_max,b)
temp=0
temp_sum=0

#수가 연속적인지, 수가 연속적이라면 temp_sum=5가 됨
for i in num_list:
    if i == 1 and temp == 0:
        temp_sum+=1
    elif i == 1 and temp == 1:
        temp_sum+=1
    elif temp == 1 and i == 0:
        break
    temp=i

if color_equal==4:
    if temp_sum==5:
        answer=num_max+900
    else:
        answer=num_max+600
else:
    if temp_sum==5:
        answer=num_max+500
    elif num_list.count(4)==1:
        answer=num_list.index(4)+800
    elif num_list.count(3)==1:
        a=num_list.index(3)
        if num_list.count(2)==1:
            answer=a*10+num_list.index(2)+700
        else:
            answer=a+400
    elif num_list.count(2)==2:
        for i in range(len(num_list)-1,0,-1):
            if num_list[i]==2:
                answer+=i*10+num_list.index(2)+300
                break
    elif num_list.count(2)==1:
        answer+=num_list.index(2)+200
if answer<100:
    answer+=num_max+100
    
print(answer)