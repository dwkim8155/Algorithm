from collections import deque

def solution(n, edge):

    maps = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    for i in edge:
        a, b = i
        maps[a].append(b)
        maps[b].append(a)

    q = deque()
    q.append([1,0])    
    visited[1] = 1

    while q:

        node, dist = q.popleft()

        for n in maps[node]:
            if not visited[n]:
                q.append([n,dist+1])
                visited[n] = dist+1

    return visited.count(max(visited))
