def solution(n, t, m, p):
    
    answer = ''
    
    length = t*m
    
    def n_transform(n,num):
        
        if num == 0:
            return "0"
        
        arr = []
        while num != 0:
            
            rest = num%n
            
            if rest ==10:
                rest = "A"
            elif rest ==11:
                rest = "B"
            elif rest ==12:
                rest = "C"
            elif rest ==13:
                rest = "D"
            elif rest ==14:
                rest = "E"
            elif num%n ==15:
                rest = "F"
                
            arr.append(str(rest))
            num = num//n
        
        return ''.join(reversed(arr))
    
    num = 0
    while len(answer) <= length:
        answer+= n_transform(n,num)
        num += 1
    
    return answer[p-1::m][:t]