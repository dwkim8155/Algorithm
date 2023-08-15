from copy import deepcopy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def bfs(x,y, graph):
    stack = []
    stack.append((x,y))
    visited = 1
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while stack:
        x,y = stack.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                stack.append((nx,ny))
                graph[nx][ny] = 2
                visited = 1

def count_zero(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt+=1

    return cnt

t = N*M
num_lst = [i for i in range(t)]
comb = []
for i in range(t):
    x1, y1 = divmod(i,M)
    if graph[x1][y1] !=0:
        continue
    for j in range(i+1,t):
        x2, y2 = divmod(j,M)
        if graph[x2][y2] !=0:
            continue
        for k in range(j+1,t):
            x3, y3 = divmod(k,M)
            if graph[x3][y3] !=0:
                continue
            comb.append((i,j,k))

max_val = 0
for c in comb:
    arr = deepcopy(graph)
    visited = [[0]*M for _ in range(N)]    

    for w in c:
        wx, wy = divmod(w,M)
        arr[wx][wy]=1

    for sx in range(N):
        for sy in range(M):
            if arr[sx][sy] == 2 and visited[sx][sy]==0:
                bfs(sx, sy, arr)

    saf_num = count_zero(arr)
    if saf_num > max_val:
        max_val = saf_num

print(max_val)