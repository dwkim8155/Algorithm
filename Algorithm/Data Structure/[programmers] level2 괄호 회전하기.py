from collections import deque

def solution(s):
    
    left_list = ["[","{","("]
    right_list = ["]","}",")"]
    
    def check(str):
        
        nonlocal left_list, right_list
        
        arr = []
        
        for i in str:
    
            if not arr:
                if i in right_list:
                    return False
    
            if i in left_list:
                arr.append(i)
            else:
                if left_list.index(arr[-1]) == right_list.index(i):
                    arr.pop()
                else:
                    return False
        
        if arr :
            return False
        else: 
            return True
    
    ans=0
    deq = deque(list(s))
    
    if check(deq):
        ans+=1
    
    for _ in range(1,len(s)):
        deq.append(deq.popleft())
        if check(deq):
            ans+=1
            
    return ans