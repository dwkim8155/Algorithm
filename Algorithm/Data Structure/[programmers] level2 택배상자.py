def solution(order):
    
    stack = []
    cnt = 0
    i = 1
    idx = 0
    
    while i <= len(order):
        
        stack.append(i)
        
        
        while stack and stack[-1] == order[idx]:
            idx+=1
            cnt+=1
            stack.pop()
        
        i+=1
    
    
    return cnt
        