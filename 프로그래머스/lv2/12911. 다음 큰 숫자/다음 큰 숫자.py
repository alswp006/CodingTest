def solution(n):
    one=str(bin(n)).count("1")
    n+=1
    while one!=str(bin(n)).count("1"):n+=1
    return n