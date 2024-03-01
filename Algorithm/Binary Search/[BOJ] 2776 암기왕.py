def binary_search(arr, num):
  s = 0
  e = len(arr)-1
  while s<=e:
    mid = (s+e)//2
    if arr[mid]<num:
      s = mid+1
    elif arr[mid]>num:
      e = mid-1
    else:
      return 1
  return 0 

T = int(input())
for _ in range(T):
  N = int(input())
  arr1 = list(map(int, input().split()))
  arr1.sort()
  M = int(input())
  arr2 = list(map(int, input().split()))
  for i in arr2:
    print(binary_search(arr1,i))