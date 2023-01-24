def solution(n):

    dp = [[[[[i,j]] if i!=j else [0] for j in range(4)] for i in range(4)] for _ in range(n+1)]
    print(dp)

    for k in range(2,n+1):
        for i in range(1,4):
            for j in range(1,4):
                if i!=j:
                    dp[k][i][j] = dp[k-1][i][6-(i+j)] +dp[k][i][j] + dp[k-1][6-(i+j)][j]


    return dp[n][1][3]