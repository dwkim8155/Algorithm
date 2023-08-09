import sys
input = sys.stdin.readline

def cal(N, total, k):

    global arr

    if N==0:
        print(" ".join(map(str, total)))
        return

    for i in range(k, len(arr)):
        total.append(arr[i])
        cal(N-1, total[:], i+1)
        total.pop()

while True:
    input_lst = list(map(int, input().split()))
    if input_lst[0] == 0:
        break
    arr = input_lst[1:]
    cal(6, [], 0)
    print()



       
