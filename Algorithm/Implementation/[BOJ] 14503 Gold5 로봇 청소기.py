N, M = map(int, input().split())
r,c,d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
move_dict = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}

answer = 0

def search(x,y):
    flag = False
    for i in range(4):
        dx, dy = move_dict[i]
        nx, ny = x+dx, y+dy
        if graph[nx][ny] == 0:
            flag = True
            break
    return flag
        

graph[r][c] = -1
answer +=1

while True:

    flag = search(r,c)
    if flag:
        for _ in range(4):
            d = (d+3)%4
            dr, dc = move_dict[d]
            nr, nc = r+dr, c+dc
            if graph[nr][nc] == 0:
                break
        r, c = nr, nc
        graph[r][c] = -1
        answer += 1  
    else:
        bd = (d+2)%4
        dr, dc = move_dict[bd]
        nr, nc = r+dr, c+dc
        if graph[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(answer)