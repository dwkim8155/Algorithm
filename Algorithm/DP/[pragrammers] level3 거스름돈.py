def solution(n, money):
    
    dp = [1] + [0]*n
    
    for m in money:
        for rest in range(m, n+1):
            dp[rest] = dp[rest] + dp[rest-m]
    
    return dp[n]%1000000007