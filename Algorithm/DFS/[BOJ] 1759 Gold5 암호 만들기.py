import sys

input = sys.stdin.readline

L,C = map(int, input().split())
P_list = sorted(input().split())
tmp = []
A_list = ["a","e","i","o","u"]
visited = [0]*C

def dfs(px,step):
    
    if step == L:
        mo = 0
        ja = 0
        for k in tmp:
            if k in A_list:
                mo+=1
            else:
                ja+=1
        if mo >= 1 and ja >=2:
            print(''.join(sorted(tmp)))
        return
            
    
    for i in range(px,C):
        if visited[i] == 0:
            tmp.append(P_list[i])
            visited[i]=1
            dfs(i+1,step+1)
            tmp.pop()
            visited[i]=0

dfs(0,0)
            
        
        
        
    
