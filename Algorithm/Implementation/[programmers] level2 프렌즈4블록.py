def solution(m, n, board):
    
    arr = [list(i) for i in board]
    
    def check(m,n,arr):
        idx_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if arr[i][j] == arr[i][j+1]==arr[i+1][j]==arr[i+1][j+1]!=0:
                    idx_set.add((i,j))
                    idx_set.add((i,j+1))
                    idx_set.add((i+1,j))
                    idx_set.add((i+1,j+1))
        return idx_set
    
    
    def rearrange(m,n,arr):
        for j in range(n):
            que = []
            for i in range(m-1,-1,-1):
                if arr[i][j] == 0:
                    que.append((i,j))
                else:
                    if que:
                        qi, qj = que.pop(0)
                        arr[qi][qj] = arr[i][j]
                        arr[i][j] = 0
                        que.append((i,j))
    ans = 0                    
    while True:
        idx_set = check(m,n,arr)
        if idx_set:
            
            ans+=len(idx_set)
        
            for i,j in idx_set:
                arr[i][j] = 0
            rearrange(m,n,arr)
        
        else:
            break
    
    return ans