def solution(n):
    # 이진수 변환 후 1의 개수 구하는 함수
    def one_cnt(x):
        Bin = bin(x)[2:]
        cnt = Bin.count("1")
        print(Bin,cnt)
        return cnt
    
    # n을 하나씩 증가시키면서 1의 개수 비교
    next_num = n+1
    while True:
        if one_cnt(n) == one_cnt(next_num):
            break
        next_num+=1

    return next_num