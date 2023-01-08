def solution(elements):
    
    answer = set()
    
    for i in range(1,len(elements)+1):
        arr = elements*2
        for j in range(len(elements)):
            answer.add(sum(arr[j:j+i]))
        
    
    
    return len(answer)