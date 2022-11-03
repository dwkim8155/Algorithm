import sys

input = sys.stdin.readline

N, M, K = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(px, py, step, total):
    global answer, K
    
    if step == K:
        answer = max(answer, total)
        return 
    
    for x in range(px,N):
        for y in range(py if x == px else 0, M):
            if visited[x][y] == 0:
                
                ok = True
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<M and visited[nx][ny]:
                        ok = False
                if ok:
                    visited[x][y] = 1
                    dfs(x,y,step+1,total+graph[x][y])
                    visited[x][y] = 0

dfs(0,0,0,0)

print(answer)
    
