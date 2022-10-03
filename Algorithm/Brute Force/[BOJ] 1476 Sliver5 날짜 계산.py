E, S, M = map(int, input().split())

arr = [0,0,0]

cnt = 0

while True:

    cnt +=1

    if arr[0] < 15:
        arr[0] +=1
    else:
        arr[0] = 1
    
    
    if arr[1] < 28:
        arr[1] += 1
    else:
        arr[1] = 1
        
    if arr[2] < 19:
        arr[2] += 1
    else:
        arr[2] = 1
        
    if arr[0] == E and arr[1] == S and arr[2] == M:
        break
    
print(cnt)