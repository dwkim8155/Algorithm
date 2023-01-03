import math

def solution(fees, records):
    
    def min_num(str_t):
        val = int(str_t[:2])*60 + int(str_t[3:])
        return val
   
    dic = dict()
    
    arr = sorted(list(map(lambda x : x.split(), records)), key = lambda x : int(x[1]))
    
    for i in arr:
        if i[2] == 'IN':
            dic[i[1]] = dic.get(i[1],0) - min_num(i[0])
        else:
            dic[i[1]] += min_num(i[0])
    
    result = []
    
    for car_num in dic:
        
        num = 0
        
        if dic[car_num] <=0:
            dic[car_num] += min_num("23:59")
        
        if dic[car_num] <= fees[0]:
            num = fees[1]
        else:
            num = fees[1] + math.ceil((dic[car_num]-fees[0]) / fees[2])*fees[3]
        
        result.append(num)
    
    
    return result