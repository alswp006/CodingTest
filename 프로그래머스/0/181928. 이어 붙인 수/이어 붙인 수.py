def solution(num_list):
    num1 = 0
    num2 = 0
    
    for i in num_list:
        if i % 2 == 0:
            num1 = num1 * 10 + i
        else :
            num2 = num2 * 10 + i
    return num1 + num2