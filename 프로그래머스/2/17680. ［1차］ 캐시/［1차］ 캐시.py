from collections import deque

def search(q, city):
    temp = deque()
    
    while q:
        x = q.popleft()
        if x == city: continue
        temp.append(x)
    
    return temp
    
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    temp_set = set()
    
    for i in range(len(cities)):
        city = cities[i].upper()
        if len(temp_set) < cacheSize:
            if city in temp_set:
                cache = search(cache, city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                temp_set.add(city)
                answer += 5
        else:
            if city in temp_set:
                cache = search(cache, city)
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                cache.popleft()
                temp_set = set(cache)
                answer += 5
    return answer