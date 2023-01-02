import heapq 

def solution(scoville, K):
    
    # heapq 만들기
    heapq.heapify(scoville)
    
    # 최소값 pop하며 반복하기
    ans = 0
    while scoville[0] < K:
        
        if len(scoville) == 1 :
            return -1
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        ans+=1
    
    return ans