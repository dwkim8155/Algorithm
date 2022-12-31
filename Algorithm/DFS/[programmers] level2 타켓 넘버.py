def solution(numbers, target):
    
    ans = 0
    visited = [0]*len(numbers)
    
    def dfs(total, step):
        
        nonlocal ans
        
        if step >=1:
            if not visited[step-1]:
                 return
        
        if step == len(numbers):
            if total == target:
                ans+=1
            return
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                for j in [-1,1]:
                    dfs(total+numbers[i]*j, step+1)
                visited[i] =0
    
    dfs(0,0)
            
    return ans