from collections import Counter

def solution(want, number, discount):
    
    ans = 0
    dic = {}
    for idx, good in enumerate(want):
        dic[good] = number[idx]
    
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            ans+=1
            
    return ans