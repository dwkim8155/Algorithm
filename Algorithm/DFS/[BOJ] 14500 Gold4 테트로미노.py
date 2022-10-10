import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
max_val = max(map(max, graph))
dx = [1,0,-1,0]
dy = [0,-1,0,1]
ans = 0



def dfs(x,y,step,total):
    global max_val,ans
    
    if total + max_val*(4-step) <= ans:
        return 
    
    if step == 4:
        ans = max(total, ans)
        return
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
            if step == 2:
                visited[nx][ny] = True
                dfs(x,y,step+1,total+graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx,ny,step+1,total+graph[nx][ny])
            visited[nx][ny] = False                  
    
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
        
print(ans)    
    
        
     
 