N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

w_num = 0
b_num = 0

def cal(x,y,N):

    global w_num, b_num, arr

    t = arr[x][y]
    for i in range(N):
        for j in range(N):
            if t != arr[x+i][y+j]:
                for r in range(2):
                    for c in range(2):
                        cal(x+(N//2)*r, y+(N//2)*c, N//2)
                return

    if t == 0:
        w_num+=1
    else:
        b_num+=1

cal(0,0,N)
print(w_num)
print(b_num)