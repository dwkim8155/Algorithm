N = int(input())

arr = [list(input()) for i in range(N)]

def check(arr):
    
    answer = 1
    
    for i in range(N):
        cnt = 1
        for j in range(N):
            if j+1 < N:
                if arr[i][j] == arr[i][j+1]:
                    cnt+=1
                else:
                    cnt = 1

                if answer < cnt:
                    answer = cnt

        cnt = 1
        for j in range(N):
            if j+1 <N:
                if arr[j][i] == arr[j+1][i]:
                    cnt+=1
                else:
                    cnt =1
                
                if answer < cnt:
                    answer = cnt
              
    
    return answer



result = 1


for i in range(N):
    
    for j in range(N-1):
            
            if arr[i][j] != arr[i][j+1]:
                arr[i][j],arr[i][j+1] = arr[i][j+1], arr[i][j]
                if result < check(arr):
                    result = check(arr)
                
                arr[i][j],arr[i][j+1] = arr[i][j+1], arr[i][j]
            
            if arr[j][i] != arr[j+1][i]:
                arr[j][i],arr[j+1][i] = arr[j+1][i], arr[j][i]
                if result < check(arr):
                    result = check(arr)
                
                arr[j][i],arr[j+1][i] = arr[j+1][i], arr[j][i]
            
print(result) 







