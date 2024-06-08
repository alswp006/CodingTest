def solution(str1, str2):
    arr1 = [str1[i:i+2].lower() for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2].lower() for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]
    A = len(arr1)
    B = len(arr2)
    AnB = 0

    for i in arr1:
        if i in arr2:
            arr2.remove(i)
            AnB += 1
    AuB = A + B - AnB
    J = lambda A, B : int(65536*A/B) if B!= 0 else 65536
    
    return J(AnB, AuB)