def solution(n):
    num1, num2= 1,2
    for i in range(n-2):
        num1, num2 = num2, num1 + num2
    return num2 % 1234567 if n != 1 else 1
