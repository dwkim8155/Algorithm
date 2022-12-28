def solution(denum1, num1, denum2, num2):
   
    defrac, frac = denum1*num2+denum2*num1, num1*num2
    
    def gcd(a,b):
        
        while b != 0:
            a, b = b, a%b
            
        return a

    answer = [i//gcd(defrac, frac) for i in [defrac, frac]]
    
    return answer