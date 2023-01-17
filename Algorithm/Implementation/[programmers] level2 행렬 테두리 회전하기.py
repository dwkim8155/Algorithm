def solution(rows, columns, queries):
    maps = [[j for j in range(i*columns+1, i*columns+columns+1)] for i in range(rows)]
    
    def rotate(arr):
        
        nonlocal maps
        
        x1,y1,x2,y2 = arr
        h_len = y2-y1
        v_len = x2-x1
        
        x,y = x1-1, y1-1
        stack = []
        stack.append(val:=maps[x][y])
         
        for ro in range(4):
            
            if ro%4 == 0:
                for _ in range(h_len):
                    y+=1
                    val= min(val, maps[x][y])
                    stack.append(maps[x][y])
                    maps[x][y] = stack.pop(0)
                    
            elif ro%4 ==1:
                for _ in range(v_len):
                    x+=1
                    val= min(val, maps[x][y])
                    stack.append(maps[x][y])
                    maps[x][y] = stack.pop(0)
                    
            elif ro%4 ==2:
                for _ in range(h_len):
                    y-=1
                    val= min(val, maps[x][y])
                    stack.append(maps[x][y])
                    maps[x][y] = stack.pop(0)
            
            elif ro%4 ==3:
                for _ in range(v_len):
                    x-=1
                    val= min(val, maps[x][y])
                    stack.append(maps[x][y])
                    maps[x][y] = stack.pop(0)
            
        return val
    
    return [rotate(q) for q in queries]