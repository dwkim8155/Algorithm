import math

def solution(n, stations, w):
    
    cnt =0
    start = 0
    std = 2*w+1
    
    for i in stations:
        end= i-w
        r = end - start-1
        if r >0:
            cnt += math.ceil(r/std)
        start = i+w
    
    if start <n:
        cnt +=math.ceil((n-start)/std)


    return  cnt 