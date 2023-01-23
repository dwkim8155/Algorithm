def solution(n, s, a, b, fares):
    
    maps = [[float('inf') if i!=j else 0 for j in range(n+1)] for i in range(n+1)]
    ans = float('inf')
    
    for fare in fares:
        no1,no2,c = fare
        maps[no1][no2] = c
        maps[no2][no1] = c
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                maps[i][j] = min(maps[i][j], maps[i][k] + maps[k][j])
    
    for i in range(1,n+1):
        ans = min(ans, maps[s][i] + maps[i][a] + maps[i][b])
    
    return ans