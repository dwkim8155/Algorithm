import re

def solution(numbers):
    
    def f(n):
        bit = bin(n)
        if bit[-1] =="0":
            return n+1
        else:
            one_num = len(re.search("1+$",bit).group())
            return n+2**(one_num-1)
        
    return list(map(f,numbers))