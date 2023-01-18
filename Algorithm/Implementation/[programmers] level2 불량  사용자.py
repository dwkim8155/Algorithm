from itertools import product

def solution(user_id, banned_id):
    
    arr = [[] for _ in range(len(banned_id))]
    
    for idx, b_id in enumerate(banned_id):
        for u_id in user_id:
            if len(b_id) != len(u_id):
                continue
            for i, j in zip(b_id, u_id):
                if i.isalpha() and i != j:
                    break
            else:
                arr[idx].append(u_id)
    
    result = []
    for i in product(*arr):
        s = set(i)
        if len(s) == len(banned_id) and s not in result:
            result.append(s)
    
    return len(result)