H = input()
S = input()

H_arr = list(H.replace(':',''))
S_arr = list(S.replace(':',''))

def Total_S(arr):
    h = int(''.join(arr[:2]))
    m = int(''.join(arr[2:4]))
    s = int(''.join(arr[4:]))
    T = h*60*60 + m*60 + s
    return T

def Time(result):
    H = result//3600
    M = (result-(H*3600))//60
    S = result-(H*3600)-(M*60)
    
    if len(str(H)) == 1:
        H = '0'+str(H) 
    if len(str(M)) == 1:
        M = '0'+str(M)     
    if len(str(S)) == 1:
        S = '0'+str(S) 
    print(f'{H}:{M}:{S}')

H_t = Total_S(H_arr)
S_t = Total_S(S_arr)

if H_t > S_t:
    result = 24*60*60 - (H_t - S_t)  
else: 
    result = S_t - H_t
 
Time(result)