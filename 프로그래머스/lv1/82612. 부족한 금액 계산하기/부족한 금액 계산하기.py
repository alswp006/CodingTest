def solution(price, money, count):
    return max(0,price*sum(range(count+1))-money)