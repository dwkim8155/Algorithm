dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    


T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])
    