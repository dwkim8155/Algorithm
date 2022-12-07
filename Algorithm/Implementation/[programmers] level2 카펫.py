def solution(brown, yellow):
    divior_list = [(yellow//i,i) for i in range(1, int(yellow**0.5)+1,) if yellow%i == 0]
    
    for i in divior_list:
        if sum(i)*2 == brown-4:
            answer = [i[0]+2,i[1]+2] 
            break