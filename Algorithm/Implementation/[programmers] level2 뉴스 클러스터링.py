import copy

def solution(str1, str2):
    
    answer = 65536
    
    arr1 = [str1[i-1:i+1].upper() for i in range(1,len(str1)) if str1[i-1:i+1].isalpha()]
    arr2 = [str2[i-1:i+1].upper() for i in range(1,len(str2)) if str2[i-1:i+1].isalpha()]
       
    if arr1 or arr2:
        
        dic1 = dict()
        dic2 = dict()
        
        for i in arr1:
            dic1[i] = dic1.get(i,0) + 1
        
        for j in arr2:
            dic2[j] = dic2.get(j,0) + 1
            
        un_dic = copy.deepcopy(dic2) 
        for i in dic1:
            if i in dic2:
                un_dic[i] = max(dic1[i],dic2[i])
            else:
                un_dic[i] = dic1[i]
                
        inter_dic = dict()
        for i in dic1:
            if i in dic2:
                inter_dic[i] = min(dic1[i],dic2[i])
        
        
        answer = int((sum(inter_dic.values())/sum(un_dic.values()))*65536)            
    
    
    return answer 