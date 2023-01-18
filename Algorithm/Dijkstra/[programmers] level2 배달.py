import heapq

def solution(N, road, K):
    
    maps = [[] for _ in range(N+1)]
    dist = [float('inf')]*(N+1)
    dist[1] = 0
    
    for i in road:
        a,b,c = i
        maps[a].append([b,c])
        maps[b].append([a,c])
        
    #dijkstra
    h = [[1,0]]
    
    while h:
        
        node, cost = heapq.heappop(h)
        
        for n, c in maps[node]:
            if cost+c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(h,[n,cost+c])
    
    return len([i for i in dist if i <=K])
    