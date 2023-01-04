import heapq 

def solution(operations):
    heap = []
    arr = [x.split() for x in operations]
    for i in arr:
        if i[0] == 'I':
            heapq.heappush(heap,int(i[1]))
        else:
            if i[1] == '1'and heap:
                max_heap = [-1*num for num in heap]
                heapq.heapify(max_heap)
                heapq.heappop(max_heap)
                heap = [num*-1 for num in max_heap]
                heapq.heapify(heap)
            else: 
                if heap:
                    heapq.heappop(heap)

    if not heap:
        ans = [0,0]
    else:
        ans = [max(heap),min(heap)]

    return ans
