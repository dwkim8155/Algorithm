from functools import reduce

def solution(clothes):
    
    dic = dict()
    
    for i in clothes:
        a, b = i
        dic[b] = dic.get(b,0) + 1
    
    arr = [i+1 for i in list(dic.values())]
    ans = reduce(lambda x,y: x*y, arr)

    return ans-1