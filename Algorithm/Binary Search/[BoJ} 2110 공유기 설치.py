import sys

input = sys.stdin.readline

N, C = map(int, input().split())

arr = [int(input()) for _ in range(N)] 
arr.sort()

end = arr[-1] - arr[0]
start = 1

while start<=end:
    current = arr[0]
    cnt = 1
    
    mid = (start+end)//2
    
    for i in range(1,len(arr)):
        if arr[i] >= (current+mid):
            cnt+=1
            current = arr[i]
    
    if C <= cnt:
        start = mid + 1
    else: 
        end = mid - 1
        
print(end)
    
            












