def solution(n, results):

    map = [[0]*n for _ in range(n)]

    for r in results:
        a, b = r
        map[a-1][b-1] = 1
        map[b-1][a-1] = -1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if map[j][i] == 0:
                    continue
                if map[j][i] == map[i][k]:
                    map[j][k] = map[j][i]
    answer = 0
    for m in map:
        cnt = 0
        for rel in m:
            if rel == 0:
                cnt+=1
        if cnt == 1:
            answer+=1

    return answer