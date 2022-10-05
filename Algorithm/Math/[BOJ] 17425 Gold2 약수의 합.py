import sys

input = sys.stdin.readline

max = 1000000

dp = [0]*(max+1)
g = [0]*(max+1)

for i in range(1,max+1):
    j = 1
    while i*j <=max:
        dp[i*j] += i
        j +=1
    
    g[i] = g[i-1] + dp[i]

T = int(input())

for _ in range(T):
    N = int(input())
    sys.stdout.write(str(g[N])+'\n') 
    