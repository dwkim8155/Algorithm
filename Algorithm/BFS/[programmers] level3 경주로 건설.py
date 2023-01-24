from collections import deque

def solution(board):
    n = len(board)
    dp = [[[float('inf')]*n for _ in range(n)] for _ in range(4)]
    
    que = deque()
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    que.append((0,0,0,0))

    while que:
        
        x,y,d,c = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n: 
                
                if board[nx][ny] ==1:
                    continue
                
                cost = c + (100 if (x,y)==(0,0) or (d+i)%2==0 else 600)
                    
                if cost < dp[i][nx][ny]:
                    dp[i][nx][ny] = cost
                    que.append((nx,ny,i,cost))
   
    return min(dp[i][n-1][n-1] for i in range(4))