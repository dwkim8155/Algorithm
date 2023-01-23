def solution(tickets):
    ans = []

    def dfs(start, arr, tickets):

        if not tickets:
            ans.append(arr)
            return


        for idx,t in enumerate(tickets):
            if t[0] == start:
                dfs(t[1],arr+[t[1]], tickets[:idx]+tickets[idx+1:])

    dfs('ICN', ['ICN'], tickets)

    return sorted(ans)[0]  