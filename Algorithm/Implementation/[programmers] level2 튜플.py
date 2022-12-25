def solution(s):
    
    arr = [i.split(",") for i in list(s[2:-2].split("},{"))]
    
    dic = dict()
    
    for i in arr:
        dic[len(i)] = dic.get(len(i),[]) + i
    
    ord_arr =  sorted(dic.items())
    
    result = [ord_arr[0][1][0]]
    
    for i in range(1,len(ord_arr)):
        tmp = set(ord_arr[i][1]) - set(result)
        result.append(list(tmp)[0])
        
    ans = list(map(int, result))
    
    return ans