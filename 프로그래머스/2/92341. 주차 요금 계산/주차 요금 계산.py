def calcul_minute(start, end):
    start = list(map(int, start.split(":")))
    end = list(map(int, end.split(":")))
    return end[1] - start[1] + 60 * (end[0] - start[0])

def solution(fees, records):
    answer = []
    result = dict()
    cars = dict()
    for i in records:
        time, car_num, status = i.split()
        if status == "IN":
            cars[car_num] = time
            if not car_num in result:
                result[car_num] = 0
        else :
            result[car_num] += calcul_minute(cars[car_num], time)
            del(cars[car_num])
    for k,v in cars.items():
        result[k] += calcul_minute(v,"23:59")
    
    for k,v in result.items():
        result[k] = fees[1] + (v - fees[0]) // fees[2] * fees[3] if v - fees[0] > 0 else fees[1]
        if v - fees[0] > 0 and (v - fees[0]) % fees[2] > 0 : result[k] += fees[3]
    
    return [i[1] for i in sorted(result.items(), key = lambda x:x[0])]