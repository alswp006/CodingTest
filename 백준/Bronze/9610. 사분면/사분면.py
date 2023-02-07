n=int(input())
arr=[0]*5
for i in range(n):
    x,y=map(int,input().split())
    if x==0 or y==0:arr[0]+=1
    elif x>0 and y>0:arr[1]+=1
    elif x<0 and y>0:arr[2]+=1
    elif x<0 and y<0:arr[3]+=1
    elif x>0 and y<0:arr[4]+=1
for i in range(1,len(arr)):
    print("Q{0}: {1}".format(i,arr[i]))
print("AXIS: {0}".format(arr[0]))