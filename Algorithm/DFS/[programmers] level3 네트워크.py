def solution(n, computers):
    
    visited = [0]*n
    
    def dfs(start):
        
        nonlocal computers
        
        visited[start] = 1
        
        for i in range(n):
            if visited[i] != 1 and computers[start][i] != 0:
                dfs(i)
    
    ans = 1
    for i in range(n):
        if visited[i] ==0:
            dfs(i)
            if sum(visited) != n:
                ans+=1
    
    
    return ans