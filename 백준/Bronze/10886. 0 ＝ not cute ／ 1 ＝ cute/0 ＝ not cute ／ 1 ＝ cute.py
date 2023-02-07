i,j=0,0
n=int(input())
for ran in range(n):
    cute=int(input())
    if cute==1:i+=1
    elif cute==0 : j+=1
if i>j:
    print("Junhee is cute!")
elif i<j :
    print("Junhee is not cute!")