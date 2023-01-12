from collections import Counter

def solution(n, works):
    
          
    while n !=0:
        
        works.sort(reverse=True)
        
        if works[0] == 0:
            break
        
        dic = Counter(works)
        arr = list(dic.items())
        
        
        if n>=arr[0][1]:
            d = arr[0][1]   
        else:
            d = n
            
        works[:d]= [works[0]-1]*d
        n-=d
        
    return sum(i**2 for i in works)