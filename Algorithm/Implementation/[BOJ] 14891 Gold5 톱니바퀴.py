from collections import deque
from copy import copy

graph = [deque(map(int, list(input()))) for _ in range(4)]
num_rotate = int(input())


def move(sx,sd):
    visited = [0]*4
    stack = []
    stack.append((sx,sd))
    
    dx = [1,-1]
    new_dict = dict()
    
    while stack:
        x, d = stack.pop(0)
        arr = copy(graph[x])
        arr.rotate(d)
        new_dict[x] = arr

        for i in range(2):
            nx = x + dx[i]
            if 0<=nx<4 and visited[nx] ==0:
                if i == 0:
                    if graph[x][2] != graph[nx][6]:
                        visited[nx] = 1                        
                        stack.append((nx,-1*d))
                else:
                    if graph[x][6] != graph[nx][2]:
                        visited[nx] = 1 
                        stack.append((nx,-1*d))

    for nl in new_dict:
        graph[nl] = new_dict[nl]

for i in range(num_rotate):
    sx, sd = map(int, input().split())
    move(sx-1,sd)

total = 0
for i in range(4):
    total += graph[i][0]*(2**i)

print(total)