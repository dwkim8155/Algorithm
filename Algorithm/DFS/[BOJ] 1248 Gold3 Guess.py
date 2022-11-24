import sys

input = sys.stdin.readline

N = int(input())
Matrix = input()
graph = []
result = []
result_list=[]
exit= False

px = 0
for i in range(N,0,-1):
    M_str = Matrix[px:px+i]
    if len(M_str) != N:
        M_str = "1"*(N-i) + Matrix[px:px+i]
    graph.append(list(M_str))
    px+=i

def check(k):
    
    global result
    
    flag = True
    result.append(k)
    for i in range(len(result)):
        tot = sum(result[i:len(result)])
        
        if tot > 0:
            tot = "+"
        elif tot < 0:
            tot = "-"
        else:
            tot= "0"
        if tot != graph[i][len(result)-1]:
            flag = False
            break
    result.pop()            
    return flag
             
def dfs(step):
    global exit,result
    
    if step == N:
        exit = True
        result_list.append(result[:])       
        return
    
    if exit == True:
        return
    
    for i in range(-10,11):
        if check(i):
            result.append(i)
            dfs(step+1)
            result.pop()
            if exit==True:
                break

dfs(0)
print(*result_list[0])