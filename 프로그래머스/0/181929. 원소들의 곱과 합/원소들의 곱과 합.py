def solution(num_list):
    num1 = 1
    num2 = 0
    for i in num_list:
        num1 *= i
        num2 += i
    return 1 if num1 < num2 ** 2 else 0