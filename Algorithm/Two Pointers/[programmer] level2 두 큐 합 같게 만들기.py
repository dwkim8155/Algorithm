def solution(queue1, queue2):
    q = queue1 + queue2
    target = sum(q) // 2

    i, j = 0, len(queue1)-1
    curr = sum(queue1)
    count = 0

    while i < len(q) and j < len(q):        
        if curr == target:
            return count

        elif curr < target and j < len(q)-1:
            j += 1
            curr += q[j]

        else:
            curr -= q[i]
            i += 1

        count += 1

    return -1

def solution(queue1, queue2):
    
    que = queue1 + queue2
    tar = sum(que) // 2
    count = 0
    start, end = 0, len(queue1)-1
    std = sum(que[start:end+1])
    
    while start < len(que) and end < len(que):
        
        if std == tar:
            return count
        
        elif std<tar and end < len(que) -1:
            end+=1
            std += que[end]
      
            
        else:
            std -= que[start]
            start+=1
            
    
        count +=1

    return -1