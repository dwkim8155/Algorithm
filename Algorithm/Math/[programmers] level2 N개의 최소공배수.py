def solution(arr):
    
    def lcm(a,b):
        
        aa = b
        bb = a%b    

        while bb!=0:
            aa,bb = bb, aa%bb
        
        lcm = a*b//aa
        
        return lcm
    
    answer = arr[0]
    
    for i in range(1,len(arr)):
        answer = lcm(answer,arr[i])
    
    return answer