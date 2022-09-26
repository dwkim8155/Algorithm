N = int(input())

memo = [0]*(N+1)

for i in range(2,N+1):
    memo[i] = memo[i-1] + 1
    
    if i%2 == 0:
        memo[i] = min(memo[i], memo[i//2] + 1)
    
    if i%3 == 0:
        memo[i] = min(memo[i], memo[i//3] + 1)
    
print(memo[N])
    














