def solution(priorities, location):
    
    idx_lst = list(range(len(priorities)))
    cnt = 0
    while True:
        
        max_idx = priorities.index(max(priorities))
        
        if max_idx != 0:
            priorities = priorities[max_idx:] + priorities[:max_idx]
            idx_lst = idx_lst[max_idx:] + idx_lst[:max_idx]
        
        if idx_lst[0] !=location:
            priorities.pop(0)
            idx_lst.pop(0)
            cnt+=1
        else:
            cnt+=1
            break
        
        
    return cnt