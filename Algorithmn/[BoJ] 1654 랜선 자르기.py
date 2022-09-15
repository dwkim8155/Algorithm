k, n = map(int, input().split())

arr_length = [int(input()) for _ in range(k)]

 
def Binary_Search(start,end,target):
    while start <= end:
        t=0
        mid = (start+end)//2
        
        for i in arr_length:
            t += i//mid
            
        if t >= n:
            start = mid + 1
        
        else:
            end = mid - 1
        
    print(end)
    
Binary_Search(1,max(arr_length),n)
            
            
            
            
            



        










