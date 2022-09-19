N = int(input())

arr = [True]*1003002
arr[1] = False
         
for i in range(2, int(1003001**0.5)+1):
    if arr[i]:
        for j in range(i**2,1003002,i):
            if arr[j]:
                arr[j] = False

for i in range(N, 1003002):
    if arr[i]:
        str_val = str(i)
        str_val_R = ''.join(list(reversed(str_val)))
        if str_val == str_val_R:
            print(str_val)
            break        
                        


        
        
            
            
            



        










