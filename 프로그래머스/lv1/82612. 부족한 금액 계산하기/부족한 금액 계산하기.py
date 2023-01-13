def solution(price, money, count):
    return price*sum(range(count+1))-money if price*sum(range(count+1))-money>0 else 0