import heapq

def solution(n, s, a, b, fares):
    
    maps = [[] for _ in range(n+1)]
    
    for fare in fares:
        n1,n2,c = fare
        
        maps[n1].append((n2,c))
        maps[n2].append((n1,c))
    
    
    def dijkstra(start):
        
        nonlocal n,maps
        
        distance = [float('inf')]*(n+1)
        distance[start[0]] = 0
        heap = []
        heapq.heappush(heap,start)
        
        while heap:
            
            node, cost = heap.pop()
            
            for no, c in maps[node]:
                if cost+c < distance[no]:
                    distance[no] = cost + c
                    heapq.heappush(heap,(no,cost+c))
        
        return distance
    
    ans = float('inf')
    visited = [0]*(n+1)
    dist = dijkstra((s,0))
    
    for i in range(1,len(dist)):
        total = dist[i]
        arr = dijkstra((i,0))
        total += arr[a]+arr[b]
        ans = min(ans, total)
    
    return ans