def solution(n):
    p_dict = {0:0, 1:1}
    for i in range(2,n+1):
        p_dict[i] = p_dict[i-1]+p_dict[i-2] 
    
    answer = p_dict[n]%1234567
    return answer