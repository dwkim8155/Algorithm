def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    
    dp[0][0] = 1
    dx = [-1,0]
    dy = [0,-1]
    
    for x in range(n):
        for y in range(m):
            
            if [y+1,x+1] in puddles:
                dp[x][y] = 0
                continue
                
            for k in range(2):
                nx = x +dx[k]
                ny = y +dy[k]
                if 0<=nx<n and 0<=ny<m:
                    dp[x][y] += dp[nx][ny]
                    
    return dp[n-1][m-1]%1000000007