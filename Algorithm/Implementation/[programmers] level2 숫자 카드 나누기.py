import math

def solution(arrayA, arrayB):  
    
    if len(arrayA) == 1:
        g_a = arrayA[0]
    else:
        g_a = math.gcd(arrayA[0],arrayA[1])
        for i in range(2,len(arrayA)):
            if g_a==1:
                break
            g_a = math.gcd(g_a,arrayA[i])
    
    if len(arrayB) == 1:
        g_b = arrayB[0]
    else:
        g_b = math.gcd(arrayB[0],arrayB[1])
        for j in range(2,len(arrayB)):
            if g_b==1:
                break
            g_b = math.gcd(g_b,arrayB[i])
    
    a_arr = [i for i in range(g_a+1,0,-1) if g_a%i==0]
    b_arr = [j for j in range(g_b+1,0,-1) if g_b%j==0]
    s = set(a_arr)&set(b_arr)
    
    a_s = sorted(set(a_arr)-s,reverse = True)
    b_s = sorted(set(b_arr)-s,reverse = True)
    
    result = []
    for A in a_s:
        flag = True
        for B in arrayB:
            if B%A==0:
                flag=False
                break
        if flag:
            result.append(A)
    
    for B in b_s:
        flag = True
        for A in arrayA:
            if A%B==0:
                flag=False
                break
        if flag:
            result.append(B)
    
    if not result:
        return 0
    else:
        return max(result)