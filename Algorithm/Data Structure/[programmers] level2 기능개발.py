def solution(progresses, speeds):
    
    result = []
    
    while progresses:
        
        progresses = [sum(i) for i in zip(progresses, speeds)]
        cnt = 0
        tmp = progresses[:]
        
        for _ in tmp:

            if progresses[0] <100:
                if cnt!=0:
                    result.append(cnt)
                break
            else:
                cnt+=1
                progresses.pop(0)
                speeds.pop(0)
        
        if not progresses:
            result.append(cnt)
        
    return result