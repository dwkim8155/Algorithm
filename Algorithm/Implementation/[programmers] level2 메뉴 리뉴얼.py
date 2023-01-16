from itertools import combinations

def solution(orders, course):   
    
    arr = list(map(lambda x: sorted(list(x)), orders))
    result = []
    
    
    for num in course:
        dic = dict()
        for order in arr:
            if len(order) >= num:
                for key in combinations(order,num):
                    dic[key] = dic.get(key,0) + 1
                    
        if not dic: 
            continue
        
        if (m:=max(dic.values())) <2:
            continue
            
        l = sorted(dic.items(), key= lambda x :x[1],reverse=True)
        for i in l:
            if i[1] == m:
                result.append("".join(i[0]))
            else:
                break

    result.sort()
    
    return result
 