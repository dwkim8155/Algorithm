def right(st):
    
    stack = []
    for i in st:
        
        if i =='(':
            stack.append(i)
        
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    
    return True
            
def uv_search(st):
    
    u = []
    
    for idx, val in enumerate(st):
        u.append(val)
        if u.count('(') == u.count(')'):
            v = st[idx+1:]       
            return ''.join(u),v
        
def solution(p):
    
    if right(p):
        return p
    
    u, v = uv_search(p)
    
    if right(u):
        return u + solution(v)
    
    else:
        new_n = ""
        for i in u[1:-1]:
            if i =='(':
                new_n+=')'
            else:
                new_n+='('
        
        return '(' + solution(v) +')' + new_n