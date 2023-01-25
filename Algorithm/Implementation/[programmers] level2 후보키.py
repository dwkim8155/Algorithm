from itertools import combinations

#후보키 포함 조합 제외하기
def pos_cand(cands,can_key,i):
    for idx in range(i):
        for k in can_key[idx]:
            if len(set(cands) - set(k)) == (len(cands) - idx):
                return False
    return True

#튜플 속성 만들기
def make_tuple(combi, arr):
    zip_list = []
    
    for idx in combi:
        zip_list.append(arr[idx])
    
    return list(zip(*zip_list))


#튜플 속성 중복 여부 확인
def check(ar):
        if len(ar) == len(set(ar)):
            return True
        
        return False
    

def solution(relation):
    
    #컬럼별 항목
    arr = list(zip(*relation))
    #컬럼의 수
    n = len(arr)
    #후보키           
    can_key = [[] for _ in range(n+1)]
     
    for i in range(1,n+1):
        
        comb = list(combinations(range(n),i))
        print(comb)
        
        for j in comb:
            if pos_cand(j,can_key,i):
                if check(make_tuple(j,arr)):
                    can_key[i].append(j)

    return sum(len(i) for i in can_key)