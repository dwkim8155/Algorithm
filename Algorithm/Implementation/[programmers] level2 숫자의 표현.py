def solution(n):
    answer = 1
    for i in range(1,(n//2)+1):
        num = i
        result = num
        while result < n:
            num+=1
            result +=num
        if result ==n:
            answer+=1 

    return answer