from heapq import heappush, heappop

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def daik(sx,ex):
    result = [float('inf')]*(N+1)
    visited= [0]*(N+1)
    heap = []
    heappush(heap, (0,sx))

    while heap:
        c, x = heappop(heap)
        if x == ex:
            return c
        visited[x] = 1
        for i in graph[x]:
            nc, nx = i
            cost = nc + c
            if visited[nx]==0:
                if cost < result[nx]:
                    result[nx] =  cost
                    heappush(heap,(cost, nx))

    return result[ex]

v1, v2 = map(int, input().split())
total = min(daik(1,v1) + daik(v1,v2) + daik(v2,N), daik(1,v2) + daik(v2,v1) + daik(v1,N)) 
if total == float('inf'):
    print(-1)
else:
    print(total)