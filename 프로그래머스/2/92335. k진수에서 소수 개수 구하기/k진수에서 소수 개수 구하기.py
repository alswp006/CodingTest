def prime_numbers(n):
    prime = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end + 1):
        if prime[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            prime[j] = 0
            
    return [i for i in prime[2:] if prime[i] != 0]

def is_prime(x):
    for i in range(2, int(x ** 0.5 + 1)):
    	if x % i == 0:
        	return False
    return True
                    
def solution(n, k):
    answer = 0
    arr = []
    prime = set(prime_numbers(1000001))

    for i in range(13, -1, -1):
        if n >= k ** i:
            temp = 0
            while n >= k ** i:
                n -= k ** i
                temp += 1
            arr.append(temp)
        else :
            if len(arr) > 0 : arr.append(0)
    temp = 0

    for i in arr:
        if i != 0 : temp = temp * 10 + i
        else:
            if temp < 1000000 and temp in prime: answer += 1
            elif temp > 1000000 and is_primenum(temp): answer += 1 
            temp = 0
    else:
        if temp < 1000000 and temp in prime: answer += 1
        elif temp > 1000000 and is_prime(temp): answer += 1
    return answer