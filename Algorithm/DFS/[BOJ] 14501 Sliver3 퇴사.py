N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
Max = 0

def dfs(day,total):
    global Max
    
    if day == N:
        Max = max(Max, total)
        return
    
    if day+arr[day][0]<=N:
        dfs(day+arr[day][0],total+arr[day][1])
    dfs(day+1,total)
    
for i in range(N):
    dfs(i,0)
print(Max)