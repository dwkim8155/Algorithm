N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
answer = ""

def tree(r, c, arr, N):

    global answer

    t = arr[r][c]
    for x in range(N):
        for y in range(N):
            if arr[r+x][c+y] != t:
                answer+="("
                for i in range(2):
                    for j in range(2):
                        tree(r+(i*N//2), c+(j*N//2), arr, N//2)
                answer+=")"
                return

    answer+= str(t)
    
tree(0, 0, arr, N)
print(answer)