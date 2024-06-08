import copy

def divide(s):
    prev = s[0].lower()
    arr=[]

    for i in s[1:].lower():
        if "a" <= i <= "z" and "a" <= prev <= "z":
            arr.append(prev+i)
        prev = i
            
    return arr

def solution(str1, str2):
    arr1 = divide(str1)
    arr2 = divide(str2)
    
    answer = 0
    result = []
    
    temp_arr2 = copy.deepcopy(arr2)
    for i in arr1:
        if i in temp_arr2:
            temp_arr2.remove(i)
            result.append(i)
    
    return int(65536 * (len(result) / (len(arr1)+len(arr2)-len(result)))) if len(arr1)+len(arr2) != 0 else 65536