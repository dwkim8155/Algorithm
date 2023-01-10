def solution(n, s):
    if n > s:
        return [-1]

    if s%n == 0:
        return [s//n]*n
    else:
        d = s%n
        arr = [s//n]*(n-d)+[(s//n)+1]*d


        return arr