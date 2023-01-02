def solution(record):

    arr = list(map(lambda x: x.split(), record))

    # 아이디:닉네임 dict 만들기
    dic_id_nick = dict()
    for i in arr:
        if i[0] in ['Enter','Change']:
            dic_id_nick[i[1]] = i[2]
 
    
    # 최종 닉네임으로 출력하기
    result = []
    for i in arr:
        if i[0] == "Enter":
            result.append(f"{dic_id_nick[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            result.append(f"{dic_id_nick[i[1]]}님이 나갔습니다.")

    
    return result