from copy import deepcopy

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def move(arr,dir):
    tmp = deepcopy(arr)
    if dir == 0:
        for j in range(N):
            p = 0
            for i in range(1,N):
                if tmp[i][j] != 0:
                    num = tmp[i][j]
                    tmp[i][j] = 0
                    if tmp[p][j] == 0:
                        tmp[p][j] = num
                    else:
                        if tmp[p][j] == num:
                            tmp[p][j]*=2
                            p+=1
                        else:
                            p+=1
                            tmp[p][j] = num
    elif dir == 1:
        for j in range(N):
            p = N-1
            for i in range(N-2,-1,-1):
                if tmp[i][j] != 0:
                    num = tmp[i][j]
                    tmp[i][j] = 0
                    if tmp[p][j] == 0:
                        tmp[p][j] = num
                    else:
                        if tmp[p][j] == num:
                            tmp[p][j]*=2
                            p-=1
                        else:
                            p-=1
                            tmp[p][j] = num
    elif dir == 2:
        for i in range(N):
            p = 0
            for j in range(1,N):
                if tmp[i][j] != 0:
                    num = tmp[i][j]
                    tmp[i][j] = 0
                    if tmp[i][p] == 0:
                        tmp[i][p] = num
                    else:
                        if tmp[i][p] == num:
                            tmp[i][p]*=2
                            p+=1
                        else:
                            p+=1
                            tmp[i][p] = num
    else:
        for i in range(N):
            p = N-1
            for j in range(N-2,-1,-1):
                if tmp[i][j] != 0:
                    num = tmp[i][j]
                    tmp[i][j] = 0
                    if tmp[i][p] == 0:
                        tmp[i][p] = num
                    else:
                        if tmp[i][p] == num:
                            tmp[i][p]*=2
                            p-=1
                        else:
                            p-=1
                            tmp[i][p] = num
    return tmp

best = 0

def solution(n, arr):
    
    global best
    
    if n==5:
        for x in range(N):
            for y in range(N):
                if best < arr[x][y]:
                    best = arr[x][y]
        return 

    for i in range(4):
        tmp = move(arr, i)
        solution(n+1, tmp)

solution(0,arr)
print(best)