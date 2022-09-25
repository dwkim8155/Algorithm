n = int(input())

memo = list(range(n+1))


def memoization_fibo(n):
    memo[0] = 0
    memo[1] = 1
    
    if n < 2:
        return memo[n]
    
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]
 
print(memoization_fibo(n))



    
        
          
    
    
 
    














