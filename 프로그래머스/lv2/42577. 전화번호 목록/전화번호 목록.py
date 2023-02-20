def solution(phone_book):
    if len(phone_book)==1:return True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i],0,len(phone_book[i]))==False:
            return False
    return True