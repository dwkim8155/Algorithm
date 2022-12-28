def solution(num, total):
    
    arr = list(range(1,num+1))
    
    diff = (total - sum(arr))//num
    
    answer = [i+diff for i in arr]
                      
    return answer