import heapq

def solution(n, costs):
    
    maps = [[] for _ in range(n)]
    ans = 0
        
    for i in costs:
        a,b,c = i
        maps[a].append((c,b))
        maps[b].append((c,a))
    
    connected = [0 for _ in range(n)]
    heap = list()
    
    heapq.heappush(heap,(0,0))
    
    while heap:
        cost, node = heapq.heappop(heap)
        
        if not connected[node]:
            ans += cost
            connected[node] = 1
        
            for c,n in maps[node]:
                if not connected[n]:
                    heapq.heappush(heap,(c,n))
    
    return ans
                