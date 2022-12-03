def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    arr = zip(A,B)
    return sum(a*b for a,b in arr) 