arr_1 = list(map(int, input()))
arr_2 = list(map(int, input()))

arr_result = []

for i in range(len(arr_1)):
    arr_result.append(arr_1[i]) 
    arr_result.append(arr_2[i])

while len(arr_result) > 2:
    arr_tmp = []
    for i in range(len(arr_result)-1):
        arr_tmp.append((arr_result[i]+arr_result[i+1])%10)
    arr_result = arr_tmp

for i in arr_result:
    print(i, end='')
        
          
    
    
 
    














