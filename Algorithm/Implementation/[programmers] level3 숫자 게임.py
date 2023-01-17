def solution(A, B):
    A.sort()
    B.sort()
    cnt = 0
    
    for i in A:
        
        while B:
            std = B.pop(0)
            if std > i:
                cnt+=1
                break
        
        if not B:
            break
            
    return cnt