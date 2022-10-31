N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [0]*N
result = []
tmp_result = []

def dfs(step):
    
    if step == M:
        if not sorted(tmp_result) in result:
            result.append(sorted(tmp_result))
        return
    
    for i in range(N):
        if not visited[i]:
            tmp_result.append(arr[i])
            visited[i] = 1
            dfs(step+1)
            tmp_result.pop()
            visited[i] = 0

dfs(0)

for i in result:
    print(*i)