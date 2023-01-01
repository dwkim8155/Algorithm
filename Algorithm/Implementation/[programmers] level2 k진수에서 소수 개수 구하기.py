def solution(n, k):
    
    #n을 k진수로 바꾸기
    def transform_k(n,k):
        list = []
        
        while n != 0 :
            list.append(str(n%k))
            n = n//k
        
        return ''.join(reversed(list))
    
    #소수 판정
    def prime_check(num):
        
        if num == 1:
            return False
            
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
    
        return True
    
    #P_list 만들기
    arr = transform_k(n,k).split("0")
    ans = 0

    for i in arr:
        if i != '':
            if prime_check(int(i)):
                ans+=1
            
    return ans