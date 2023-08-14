N = int(input())
graph = [[0]*N for _ in range(N)]
snake = []

num_apple = int(input())

for _ in range(num_apple):
    ax,ay = input().split()
    graph[int(ax)-1][int(ay)-1] = -1

num_order = int(input())
order_lst = []
for _ in range(num_order):
    t, angle = input().split()
    order_lst.append((int(t),angle))

move_dict = {0:(0,-1), 1:(0,1), 2:(-1,0), 3:(1,0)}
time_state = 0
dir_state = 1

x,y = 0, 0
snake.append((x,y))
graph[x][y] = 1

def change_dir(dir_state, o):
    if dir_state == 0:
        dir_state = 3 if o == "L" else 2
    elif dir_state == 1 :
        dir_state = 2 if o == "L" else 3
    elif dir_state == 2 :
        dir_state = 0 if o == "L" else 1    
    else:
        dir_state = 1 if o == "L" else 0
    return dir_state        


ch_time, o = order_lst.pop(0)

while True:  
    if time_state == ch_time:
        dir_state = change_dir(dir_state,o)
        if order_lst:
            ch_time, o = order_lst.pop(0)  
    
    dx, dy = move_dict[dir_state]
    x+=dx; y+=dy
    time_state+=1
    
    if x<0 or x>=N or y<0 or y>=N  or graph[x][y] == 1:
        print(time_state) 
        break
    
    if graph[x][y] != -1:
        t_x, t_y = snake.pop(0)
        graph[t_x][t_y] = 0
        
    
    graph[x][y] = 1
    snake.append((x,y))

    

