def solution(places):
    
    def search(x,y,maps):
        
        dx = [1,-1,0,0,1,1,-1,-1,2,-2,0,0]
        dy = [0,0,1,-1,1,-1,1,-1,0,0,2,-2]
        
        for i in range(12):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                
                if i//4 == 0:
                    if maps[nx][ny] == "P":
                        return False
                elif i//4 == 1:
                    if maps[nx][ny] == 'P':
                        if maps[x][ny] != 'X' or maps[nx][y] != 'X':
                            return False
                else:
                    if maps[nx][ny] == 'P':
                        if (nx-x) == 0:
                            if ny-y > 0:
                                if maps[nx][y+1] != 'X':
                                    return False
                            else:
                                if maps[nx][y-1] != 'X':
                                    return False
                        else:
                            if nx-x > 0:
                                if maps[x+1][ny] != 'X':
                                    return False
                            else:
                                if maps[x-1][ny] != 'X':
                                    return False
                            
        return True
    
    answer = []
    
    for p in places:
        flag =True                    
        for k in range(5):
            if not flag:
                break
            for l in range(5):
                if p[k][l]=='P':
                    if not search(k,l,p):
                        answer.append(0)
                        flag = False
                        break
        if flag:
            answer.append(1)
    
    return answer