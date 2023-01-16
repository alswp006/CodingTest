def solution(s):
    arr=["zero","one","two","three","four","five","six","seven","eight","nine"]
    answer = 0
    for i in range(len(arr)):
        s=s.replace(arr[i],str(i))
    print(s)
    return int(s)