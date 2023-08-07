N = int(input())
st = N//3 
arr =[list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
plus =0

def cal_num(arr, N):
    
    global minus, zero, plus

    target = arr[0][0]

    for i in arr:
        for j in i:
            if target != j and N!=1:
                for r in range(0,N,N//3):
                    for c in range(0,N,N//3): 
                        cal_num(make_arr(arr,r,c,N//3), N//3)              
                return
    
    if target == -1:
        minus+=1
    elif target == 0:
        zero+=1
    else:
        plus+=1
    

def make_arr(arr, i, j, st):
    tmp = []
    for c in arr[i:i+st]:
        tmp.append(c[j:j+st])
    return tmp
    
cal_num(arr, N)
for i in [minus ,zero, plus]:
    print(i)