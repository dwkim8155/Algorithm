n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = max(arr)
e = sum(arr)
while s<=e:
  total = 0
  count = 1
  mid = (s+e)//2
  for i in arr:
    total+=i
    if total>mid:
      count+=1
      total=i
  
  if count>m:
    s = mid+1
  else:
    e = mid-1

print(s)