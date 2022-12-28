def solution(phone_book):

    answer = True
    
    dic = dict()
    
    for p in phone_book:
        for i in range(1,len(p)):
            dic[p[:i]] = 1
    
    for p in phone_book:
        if p in dic:
            answer = False        

    return answer