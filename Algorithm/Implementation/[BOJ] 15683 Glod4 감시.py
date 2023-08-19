from copy import deepcopy

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cctv_lst = []
wall_num = 0
dir_dict = {1:[[0],[1],[2],[3]], 2:[(0,2), (1,3)], 3:[(0,1), (1,2), (2,3),(3,0)], 
            4:[(0,1,3), (0,1,2), (1,2,3), (2,3,0)], 5:[(0,1,2,3)]}

for i in range(N):
    for j in range(M):
        if 1<=graph[i][j]<=5:
            cctv_lst.append((i,j,graph[i][j]))
        elif graph[i][j] == 6:
            wall_num+=1

def move(x,y,dir,arr):
    arr[x][y] = 1
    while True:
        if dir == 0:
            x-=1
        elif dir == 1:
            y+=1
        elif dir == 2:
            x+=1
        else:
            y-=1
        
        if x<0 or x>=N or y<0 or y>=M:
            break
       
        if graph[x][y] == 6:
            break
        
        arr[x][y]=1

min_area = float('inf')

def solution(visited, n):

    global min_area

    if n == len(cctv_lst):
        result = 0
        for r in visited:
            result+=sum(r)
        result = N*M - result - wall_num
        if result < min_area:
            min_area = result    
        return
    
    x,y,cctv = cctv_lst[n]
    for d_lst in dir_dict[cctv]:
        arr = deepcopy(visited)
        for d in d_lst:
            move(x,y,d,arr)
        solution(arr, n+1)

visited = [[0]*M for _ in range(N)]
solution(visited,0)
print(min_area)