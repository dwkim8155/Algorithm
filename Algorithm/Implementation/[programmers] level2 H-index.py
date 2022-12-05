def solution(citations):
    dic = dict()
    for i in citations:
        dic[i] = dic.get(i,0) + 1
    print(dic)

    for h in range(len(citations)+1):
        cnt = 0
        for i in dic:
            if i >= h:
                cnt += dic[i]
        if h > cnt:
            return h-1
            break
    else:
        return h