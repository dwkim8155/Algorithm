import heapq

def solution(jobs):

    jobs.sort()

    n = len(jobs)
    t = jobs[0][0] +jobs[0][1]
    ans = jobs[0][1]
    jobs.pop(0)

    heap = []

    while jobs or heap:

        for i in jobs[:]:
            if i[0] <=t:
                r_t, c = jobs.pop(0)
                heapq.heappush(heap,(c,r_t))
            else:
                break

        if len(heap) >0:
            cost, time = heapq.heappop(heap)
            ans += t-time+cost
            t+=cost

        else:
            t+=1

    return ans//n
