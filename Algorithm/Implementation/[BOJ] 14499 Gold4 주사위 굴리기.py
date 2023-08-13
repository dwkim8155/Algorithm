N, M, x ,y ,num_o = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
direction = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
dice = [[0]*3 for _ in range(4)]


def roll(x,y,dir):
    if dir<=2:
        tmp_lst = ([dice[3][1]]+[dice[1][i] for i in range(3)]) if dir==1 else [dice[1][1], dice[1][2], dice[3][1], dice[1][0]]
        dice[1][0] = tmp_lst[0]
        dice[1][1] = tmp_lst[1]
        dice[1][2] = tmp_lst[2]
        dice[3][1] = tmp_lst[3]
    else:
        tmp_lst = [dice[1][1], dice[2][1], dice[3][1], dice[0][1]] if dir==3 else [dice[3][1], dice[0][1], dice[1][1], dice[2][1]]
        dice[0][1] = tmp_lst[0]
        dice[1][1] = tmp_lst[1]
        dice[2][1] = tmp_lst[2]
        dice[3][1] = tmp_lst[3]

for o in order:
    dx, dy = direction[o]
    if 0<=x+dx<N and 0<=y+dy<M:
        x+=dx; y+=dy
        roll(x,y,o)
        map_num = arr[x][y]
        if map_num == 0:
            arr[x][y] = dice[3][1]
        else:
            dice[3][1] = arr[x][y]
            arr[x][y] = 0      
        print(dice[1][1])