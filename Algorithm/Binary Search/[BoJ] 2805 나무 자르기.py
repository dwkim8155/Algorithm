N, M = map(int, input().split())

arr = list(map(int, input().split()))
       
def Binary_Search(start,end,target):
    while start<=end:
        cnt = 0
        mid = (start+end)//2
        
        for i in arr:
            if i-mid > 0:
                cnt+=i-mid
        
        if cnt>=target:
            start = mid + 1 
        else:
            end = mid - 1
    
    print(end)
    
Binary_Search(1,max(arr),M)
        
            
                
            
            
            



        










