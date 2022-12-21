def solution(s):
    s_list = list(s)
    arr = []
    answer = 1
    
    for i in s_list:
        if not arr:
            arr.append(i)
            continue
            
        if i == arr[-1]:
            arr.pop()
        else:
            arr.append(i)
    if arr:
        answer = 0

    return answer