N, M = map(int,input().split())
arr =[]

for x in range(N):
    tmp = list(input())
    arr.append(tmp)
    for y in range(M):
        if tmp[y]=="R":
            rsx, rsy = x,y
        elif tmp[y]=="B":
            bsx, bsy = x,y
        elif tmp[y]=="O":
            ox, oy = x,y

def move(x, y, dx, dy):
    cnt=0
    while arr[x+dx][y+dy] != "#" and arr[x][y] != "O":
        x+=dx
        y+=dy
        cnt+=1
    return x,y,cnt


def solution():
    visited = dict()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[(rsx,rsy, bsx, bsy)] = True
    stack = [(rsx, rsy, bsx, bsy, 0)]

    while stack:
        rnx, rny, bnx, bny ,cnt = stack.pop(0)
        
        if cnt == 10:
            return -1

        for i in range(4):
            rdx, rdy, rm_cnt = move(rnx,rny, dx[i], dy[i])
            bdx, bdy, bm_cnt = move(bnx,bny, dx[i], dy[i])
            if (bdx, bdy) != (ox,oy):
                if (rdx, rdy) == (ox, oy):
                    return cnt+1
                if (rdx, rdy) == (bdx, bdy):
                    if rm_cnt > bm_cnt:
                        rdx, rdy = rdx-dx[i], rdy-dy[i]
                    else:
                        bdx, bdy = bdx-dx[i], bdy-dy[i]
                if (rdx, rdy, bdx, bdy) not in visited:
                    visited[(rdx, rdy, bdx, bdy)] = True
                    stack.append((rdx,rdy,bdx,bdy,cnt+1))
    
    return -1

print(solution())