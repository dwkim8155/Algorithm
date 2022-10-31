N, M = map(int, input().split())
result = []

def dfs(step):
    global result,N,M
    
    if step == M:
        print(*result)
        return
    
    if len(result) == 0:
        for i in range(1,N+1):
            result.append(i)
            dfs(step+1)
            result.pop()
    else:
        for i in range(1,N+1):
            if result[-1] <= i:
                result.append(i)
                dfs(step+1)
                result.pop()
dfs(0)