N  = int(input())

arr = list(map(int,input().split()))
arr.sort()

start = 0
end = N-1
answer = abs(arr[start]+arr[end])
Final = [start, end]

while start<end:
    sum = arr[start]+arr[end]
    
    if abs(sum) < answer:
        answer = abs(sum)
        Final = [start, end]
        if sum == 0 :
            break
    
    if sum>0:
        end -= 1
    else:
        start += 1
    
print(arr[Final[0]], arr[Final[1]])
        
 
    














