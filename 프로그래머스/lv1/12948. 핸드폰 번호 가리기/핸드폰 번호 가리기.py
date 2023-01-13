def solution(phone_number):
    phone_number=list(phone_number)
    for i in range(0,len(phone_number)-4):phone_number[i]='*'
    return ''.join(phone_number)