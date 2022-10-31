N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = []

def dfs(step):
    
    if step == M:
        print(*result)
        return
    
    if len(result) == 0:
        for i in range(N):
            result.append(arr[i])
            dfs(step+1)
            result.pop()
    else:
        for i in range(N):
            if result[-1]<=arr[i]:
                result.append(arr[i])
                dfs(step+1)
                result.pop()
                
dfs(0)