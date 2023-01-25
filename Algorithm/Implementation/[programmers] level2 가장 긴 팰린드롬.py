def solution(s):
    
    def check(st):
        if st == st[::-1]:
            return True
        return False
    
    ans = []
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if check(val:=s[j:j+i]):
                return len(val)