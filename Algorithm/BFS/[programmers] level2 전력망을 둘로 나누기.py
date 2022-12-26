def solution(n, wires):

    def gra(arr):

        graph = [[] for _ in range(n+1)]

        for i in range(len(arr)):
            graph[arr[i][0]].append(arr[i][1])
            graph[arr[i][1]].append(arr[i][0])

        return graph



    def bfs(start):

        visited = [0]*(n+1)
        stack = []

        visited[start] = 1
        stack.append(start)


        while stack:
            x = stack.pop()
            for i in graph[x]:
                if not visited[i]:
                    visited[i] = 1
                    stack.append(i)

        val = abs(n-2*sum(visited))

        return val

    ans = 1000

    for i in range(len(wires)):
        graph = gra(wires[:i]+wires[i+1:])
        ans = min(bfs(wires[i][0]), ans)

    return ans