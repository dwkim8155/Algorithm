def solution(arr):
   
    m = len(arr)
    div = m
    visited = [[0]*m for _ in range(m)]
    dic = {0:0, 1:0}
    
    def search(i,j,div):
        
        nonlocal arr
        
        std =  arr[i][j]
        
        for k in range(i,i+div):
            for l in range(j,j+div):
                if arr[k][l] != std:
                    return -1
        
        return std
        
    def check(i,j,div):
        
        nonlocal visited
        
        for k in range(i,i+div):
            for l in range(j,j+div):
                visited[k][l] = 1
    

    while div != 0:
        
        
        for i in range(0,m,div):
            for j in range(0,m,div):
                if not visited[i][j]:
                    a = search(i,j, div)
                    if a != -1:
                        dic[a] += 1
                        check(i,j,div)
        div //= 2        
    
    if m == 1:
        dic[arr[0]] +=1 
    
    return [i for i in dic.values()]