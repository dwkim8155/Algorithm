from math import factorial

def solution(n, k):
    
    arr = [i for i in range(1,n+1)]
    ans = []
    
    while n != 0:
        fac = factorial(n-1)
        idx = (k-1)//fac
        ans.append(arr[idx])
        arr.pop(idx)
        n-=1
        k%=fac

    return ans 