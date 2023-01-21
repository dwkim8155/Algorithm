def solution(s):

    dic = dict()
    result = []
    for idx, key in enumerate(s):
        if key not in dic:
            result.append(-1)
        else:
            result.append(idx - dic[key])

        dic[key] = idx

    return result