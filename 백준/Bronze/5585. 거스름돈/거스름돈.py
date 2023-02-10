n=int(input())
answer=0
money=1000-n
money_type=[500,100,50,10,5,1]
for i in money_type:
    if money>=i:
        answer+=money//i
        money%=i
print(answer)