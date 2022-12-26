def solution(polynomial):
    
    arr = polynomial.split(" + ")
    
    num_int = 0
    num_var = 0
    
    for i in arr:
        if 'x' in i:
            if i == 'x':
                num_var += 1
            else:
                num_var += int(i[:-1])
        else:
            num_int += int(i)
            
    if num_int !=0 and num_var !=0:
        if num_var != 1:
            ans = str(num_var)+'x'+' + '+str(num_int)
        else:
            ans = 'x'+' + '+str(num_int)
            
    elif num_int == 0 and num_var !=0:
        if num_var != 1:
            ans = str(num_var)+'x'
        else:
            ans = 'x'
    elif num_var == 0 and num_int !=0:
        ans = str(num_int)
    return ans