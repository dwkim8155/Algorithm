import heapq

N = int(input())
arr = [int(input()) for _ in range(N)]
heapq.heapify(arr)

ans=0
while True:
  if len(arr) ==1 :
    print(ans)
    break
  num1 = heapq.heappop(arr)
  num2 = heapq.heappop(arr)
  nnum = num1+num2
  ans+=nnum
  heapq.heappush(arr, nnum)
