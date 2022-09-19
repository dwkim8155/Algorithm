N = int(input())
arr_N = list(map(int, input().split()))

M = int(input())
arr_M = list(map(int, input().split()))

dict = {}

for i in arr_N:
    dict[i] = 1
    
for i in arr_M:
    if i in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
    
        
            



        










