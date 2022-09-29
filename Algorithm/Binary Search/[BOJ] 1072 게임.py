X, Y = map(int, input().split())

origin_P = int(100*Y/X)
start = 1
end = X

if origin_P >= 99:
    print(-1)

else:
    while start<=end:
    
        mid = (start + end)//2
        P = int(100*(Y+mid)/(X+mid))
  
        if P == origin_P:
            start = mid + 1
        else:
            end = mid - 1
    print(start)
        
    
      

       
    
        









