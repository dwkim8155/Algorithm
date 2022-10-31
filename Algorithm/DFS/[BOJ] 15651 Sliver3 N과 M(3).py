import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())

result = []
tmp_arr = []


def dfs(N,M,step):
    
    if step == M:
        result.append(tmp_arr[:])
        return
    
    for i in range(1,N+1):
        tmp_arr.append(i)
        dfs(N,M,step+1)
        tmp_arr.pop() 

dfs(N,M,0)

for i in result:
    print(*i)