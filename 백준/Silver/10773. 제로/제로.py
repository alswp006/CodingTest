answer_list=[]

for i in range(int(input())):
    n=int(input())
    if n!=0:
        answer_list.append(n)
    if n==0:
        answer_list.pop()
print(sum(answer_list))