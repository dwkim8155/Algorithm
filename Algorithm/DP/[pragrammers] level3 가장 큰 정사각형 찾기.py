def solution(board):
    
    row = len(board)
    col = len(board[0])
    ans = 0
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                ans =1
                break

    for i in range(1,row):
        for j in range(1,col):
            
            if board[i][j] == 0:
                continue
                
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
            ans = max(ans, board[i][j])
    

                
    return ans**2
    