def solution(n):
    
    num_list = ["1","2","4"]
    
    ans = ""
    
    while n != 0:
        n-=1
        ans = num_list[n%3] + ans
        n//=3

    
    return ans