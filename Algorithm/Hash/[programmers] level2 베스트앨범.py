from collections import defaultdict

def solution(genres, plays):
    
    ans = []
    dic = defaultdict(lambda:[[],[]])
    
    order = sorted(enumerate(plays), key = lambda x: x[1], reverse =True)
    
    for idx,val in order:
        dic[genres[idx]][0].append(val)
        dic[genres[idx]][1].append(idx)
        
    for genre in dic:
        dic[genre].append(sum(dic[genre][0]))
    
    arr = sorted(dic.items(), key = lambda x : x[1][2], reverse = True)
    
    for genre in arr:
        ans += genre[1][1][:2]
    
    
    return ans