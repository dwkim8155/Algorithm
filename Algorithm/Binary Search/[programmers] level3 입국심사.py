def solution(n, times):
    
    start = 0
    end = max(times)*n
    
    while start <= end:
        
        mid = (start + end)//2
        
        cnt = 0
        for i in times:
            cnt+= (mid//i)
        
        if n <=cnt:
            end = mid-1
        else:
            start = mid+1
    
    return start