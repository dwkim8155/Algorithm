def solution(prices):
    
    answer = [0]*len(prices)
    stack = []
    
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            num = stack.pop()
            answer[num] = idx - num
        stack.append(idx)
    
    while stack:
        num = stack.pop()
        answer[num] = len(prices) - 1 - num 
        
    return answer