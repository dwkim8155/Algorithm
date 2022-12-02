def solution(n,a,b):

    
    def next_order(num):
        if num%2 ==0:
            next_order = num//2
        else:
            next_order = (num//2)+1
        return next_order
    
    def even_status(num):
        status =False
        if num%2 == 0:
            status = True
        return status
    
    round = 1
    
    if abs(a-b) ==1:
            if even_status(a):
                if a > b:
                    return round
                else:
                    pass
            else:
                if a<b:
                    return round
                else:
                    pass
        
    
    while True:
        round+=1
        a =  next_order(a)
        b = next_order(b)
        
        if abs(a-b) ==1:
            if even_status(a):
                if a > b:
                    break
                else:
                    pass
            else:
                if a<b:
                    break
                else:
                    pass
                
        
    return round