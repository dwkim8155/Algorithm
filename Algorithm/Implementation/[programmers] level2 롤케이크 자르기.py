from collections import Counter

def solution(topping):
    
    bro = set()
    me = Counter(topping)
    ans = 0
    
    for i in topping:
        
        bro.add(i)
        me[i] -= 1
        
        if me[i] == 0:
            del me[i]
        
        if len(bro) == len(me):
            ans+=1
    
    return ans