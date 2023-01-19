def solution(gems):

    std = len(set(gems))
    dic = dict()
    
    left = 0
    right = 0
    dic[gems[right]] = 1
    
    ans = [left, len(gems)-1]
    
    while True:
        
        if len(dic) != std:
            right+=1
            if right >=len(gems):
                break
            dic[gems[right]] = dic.get(gems[right],0) +1

        else:
            if dic[gems[left]] == 1:
                if (right-left) < (ans[1]-ans[0]):
                    ans = [left, right]
                dic.pop(gems[left])
            else:
                dic[gems[left]] -=1    
            
            left+=1
    
        
    return list(map(lambda x: x+1, ans))