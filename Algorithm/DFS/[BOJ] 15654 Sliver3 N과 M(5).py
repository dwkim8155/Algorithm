N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]*N
result = []

def dfs(step):
    
    if step == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:
            result.append(arr[i])
            visited[i] = 1
            dfs(step+1)
            result.pop()
            visited[i] = 0

dfs(0)