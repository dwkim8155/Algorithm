def solution(people, limit):
    
    people.sort()
    
    start = 0
    end = len(people)-1
    cnt = 0
    
    while start <= end:
        if people[start] + people[end]<=limit:
            end-=1
            start+=1
            cnt+=1
        else:
            end-=1
            cnt+=1
        
    return cnt