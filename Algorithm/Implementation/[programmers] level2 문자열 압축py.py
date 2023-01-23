import math

def solution(s):
    
    def transform(n,st):
        arr = []
        start = 0
        itr = math.ceil(len(st)/n)*n
        for i in range(n,itr+1,n):
            arr.append(st[start:i])
            start = i
        
        new_arr = []
        
        que = []
        while arr:
            
            que.append(arr.pop(0))
            if not arr or que[-1] != arr[0]:
                if len(que) > 1:
                    new_arr.append(str(len(que))+que[0])
                else:
                    new_arr.append(que[0])
                que.clear()
                
        return ''.join(new_arr)
            
    ans = float('inf')   
    for i in range(1,len(s)+1):
        ans = min(ans,len(transform(i,s)))
    
    return ans