N = int(input())

L = len(str(N))

dp = [0]*9
s = [0]*9

for i in range(1,9):
    dp[i] = 9*10**(i-1)*i
    s[i] = s[i-1] + dp[i]


result = s[L-1] + (N-10**(L-1)+1)*L    
print(result)