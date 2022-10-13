N, M = map(int,input().split())

visited = [0 for _ in range(N+1)]
result_arr = [] 
tmp_arr = []

def dfs(N,M,step):
    
    val = sorted(tmp_arr)
    
    if step == M:
        if not val in result_arr:
            result_arr.append(val)
            print(*val)
            return
     
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = 1
            tmp_arr.append(i)
            dfs(N,M,step+1)
            visited[i] = 0 
            tmp_arr.pop()
        
dfs(N,M,0)

