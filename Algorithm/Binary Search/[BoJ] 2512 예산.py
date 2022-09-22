N = int(input())

arr = list(map(int, input().split()))

T = int(input())

start = 1
end = T

if sum(arr) <= T:
    print(max(arr))

else:
    while start<=end:
        result = 0
        mid = (start+end)//2
    
        for i in arr:
            result += min(mid,i)
        
        if result <= T:
            start = mid + 1
        else:
            end = mid - 1

    print(end)














