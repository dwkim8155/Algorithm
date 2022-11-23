import sys

input = sys.stdin.readline

N = int(input())
Bu_list = input().split()
visited=[0]*10
result = []
Max = 0
Min = 100000000000


def dfs(x,step):
    global Max, Min
    
    if step == 0:
        visited[x] = 1
        result.append(x)
    
    if step == N:
        val = int(''.join(map(str,result[:])))
        Max = max(Max,val)
        Min = min(Min,val)
        return
        
    for i in range(10):
        if Bu_list[step] == "<":
            if x < i and not visited[i]:
                visited[i] = 1
                result.append(i)
                dfs(i,step+1)
                visited[i] = 0
                result.pop()
        else:
            if x > i and not visited[i]:
                visited[i] = 1
                result.append(i)
                dfs(i,step+1)
                visited[i] = 0
                result.pop()

for i in range(10):
    dfs(i,0)
    visited[i] = 0
    result.pop()

if len(str(Max))!= N+1:
    Max = "0" + str(Max)
if len(str(Min)) !=N+1:
    Min = "0" + str(Min)

print(Max)
print(Min)        
                

