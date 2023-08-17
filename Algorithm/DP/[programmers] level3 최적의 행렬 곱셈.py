def solution(matrix_sizes):
    N = len(matrix_sizes)
    dp = [[0]*N for _ in range(N)]

    for k in range(1,N):
        for s in range(N-k):
            e = s+k
            candi = []
            for m in range(s,e):
                candi.append(
                dp[s][m] + dp[m+1][e] + matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1])
            dp[s][e] = min(candi)

    return dp[0][-1]