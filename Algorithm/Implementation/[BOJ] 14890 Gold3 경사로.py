from copy import deepcopy

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
load = 0

def check(x,y,h,d,visited):
    flag = True

    if h=="up":
        if d =="r":
            if y-L+1 < 0:
                return False
        else:
            if x-L+1 <0:
                return False
    else:
        if d == "r":
            if y+L >= N:
                return False
        else:
            if x+L >= N:
                return False

    for i in range(L):
        if h == "up":
            st = graph[x][y]
            if d=="r":

                if graph[x][y-i]!=st or visited[x][y-i]==1:
                    flag=False
            else:
                if graph[x-i][y]!=st or visited[x-i][y]==1:
                    flag=False
            
        else:
            if d=="r":
                st = graph[x][y+1]
                if graph[x][y+1+i]!=st or visited[x][y+1+i]==1:
                    flag=False
            else:
                st = graph[x+1][y]
                if graph[x+1+i][y]!=st or visited[x+1+i][y]==1:
                    flag=False      
    return flag

def build(x,y,h,d,visited):
    for i in range(L):
        if h == "up":
            if d=="r":
                visited[x][y-i] = 1           
            else:
                visited[x-i][y] = 1
        else:
            if d=="r":
                visited[x][y+1+i] = 1
            else:
                visited[x+1+i][y] = 1

d="r"
for i in range(N):
    load_flag = True
    arr = deepcopy(visited)
    for j in range(N-1):
        pst = graph[i][j]
        nst = graph[i][j+1]
        
        if pst == nst:
            continue
        elif pst > nst:
            h="down"
        else:
            h="up"
        
        if abs(pst-nst) > 1:
            load_flag =False
            break
        
        flag = check(i,j,h,d,arr)
        if not flag:
            load_flag =False
            break
        else:
            build(i,j,h,d,arr)
            
    if load_flag:
        load+=1
        visited = arr
       

d="c"
visited = [[0]*N for _ in range(N)]
for j in range(N):
    load_flag = True
    arr = deepcopy(visited)
    for i in range(N-1):
        pst = graph[i][j]
        nst = graph[i+1][j]
        
        if pst == nst:
            continue
        elif pst > nst:
            h="down"
        else:
            h="up"
        
        if abs(pst-nst) > 1:
            load_flag =False
            break
        
        flag = check(i,j,h,d,arr)
        if not flag:
            load_flag =False
            break
        else:
            build(i,j,h,d,arr)
    
    if load_flag:
        load+=1
        visited = arr
        
print(load)
