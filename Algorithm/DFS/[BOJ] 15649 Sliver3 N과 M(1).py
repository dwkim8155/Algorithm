N, M = map(int, input().split())
visited = [0]*(N+1)
ans_arr = []

def dfs(N,M,step):
    
    global ans_arr
    
    if step == M:
        print(*ans_arr)
        return 
        
    for i in range(1,N+1):
    
        if not visited[i]:
            ans_arr.append(i)
            visited[i] = 1
            dfs(N,M,step+1)
            ans_arr.pop()
            visited[i] = 0

dfs(N,M,0)