def solution(k, dungeons):

    answer = -1

    def dfs (k, arr1, arr2):

        nonlocal answer

        answer = max(len(arr1), answer)

        for i in range(len(arr2)):
            if k >= arr2[i][0]:
                dfs(k-arr2[i][1], arr1+[arr2[i]], arr2[:i] + arr2[i+1:])

    dfs(k,[],dungeons)

    return answer