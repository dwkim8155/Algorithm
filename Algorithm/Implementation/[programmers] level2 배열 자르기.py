def solution(n, left, right):
    
    answer=[]
    
    for i in range(left,right+1):
        row = i//n
        col = i%n
        if row > col:
            val = row+1
        else:
            val = col+1
        
        answer.append(val)
        
    return answer