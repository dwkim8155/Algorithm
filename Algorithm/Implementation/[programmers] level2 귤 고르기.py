def solution(k, tangerine):

    # 빈도수 딕셔너리 만들기
    dic = dict()
    for i in tangerine:
        dic[i] = dic.get(i,0) + 1

    # 내림차순 정렬
    arr = sorted(dic.items(), key = lambda x : x[1], reverse = True)

    # 종류 count
    ans=1
    for i in arr:
        k-=i[1]
        if k > 0:
            ans+=1

    return ans