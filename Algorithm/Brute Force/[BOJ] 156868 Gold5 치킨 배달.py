def distance(chickCord, houseCord):
  cx, cy = chickCord
  hx, hy = houseCord
  return abs(cx-hx) + abs(cy-hy)

def chickDistance(hcord, cArr):
  return min(distance(cc,hcord) for cc in cArr)


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')         

cArr = []
hArr = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == 2:
      cArr.append((i,j))
    elif graph[i][j] == 1:
      hArr.append((i,j))


def solution(sArr, m, sIdx):
  global M, hArr, cArr, ans
  
  if m==M:
    total = 0
    for hc in hArr:
      total += chickDistance(hc, sArr)
    if total<ans:
      ans = total
    return   
  
  for i in range(sIdx, len(cArr)):
    nsArr = sArr+[cArr[i]]
    solution(nsArr,m+1,i+1)
    
  
  
solution([],0,0)
print(ans)