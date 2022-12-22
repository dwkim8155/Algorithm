def solution(arr1, arr2):
    row_len = len(arr1[0])
    arr2 = list(zip(*arr2))
    Matrix =[[sum(a*b for a,b in zip(i,j)) for j in arr2] for i in arr1]
    return Matrix