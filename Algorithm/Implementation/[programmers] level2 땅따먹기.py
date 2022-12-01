
def solution(land):
    result = land[0]
    for i in land[1:]:
        max_cnt = max(result)
        max_idx = result.index(max_cnt)
        result_tmp = result[:]
        for j in range(4):
            if j != max_idx:
                result[j] = i[j] + max_cnt
            else:
                result_tmp[max_idx] = 0
                result[j] = i[j]+ max(result_tmp)

    return max(result)


