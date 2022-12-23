from itertools import permutations

def solution(numbers):

    def prime_check(n):

        flag = True

        if n ==1 or n==0:
            flag= False
            return flag

        for i in range(2,int(n**0.5)+1):
            if n%i ==0:
                flag = False
                break

        return flag

    arr = list(numbers) 
    result = []

    for i in range(1,len(arr)+1):
        perm_set = set(permutations(arr,i))
        for j in perm_set:
            val = int(''.join(j))
            if prime_check(val) and not val in result:
                result.append(val)

    return len(result)