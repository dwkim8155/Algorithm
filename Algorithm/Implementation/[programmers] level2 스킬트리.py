def solution(skill, skill_trees):

    cnt = 0
    for i in skill_trees:

        que = list(skill)

        for j in i:

            if j in que:
                if que.pop(0) != j:
                    break
        else:
            cnt+=1



    return cnt