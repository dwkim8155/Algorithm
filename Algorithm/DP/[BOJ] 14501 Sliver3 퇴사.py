N = int(input())

visited = [0 for _ in range(N+1)]
arr = []

max = 0
day = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

def dfs(N,day):
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            
        