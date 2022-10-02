arr = [int(input()) for i in range(9)]

arr.sort()
Break = True

C = sum(arr) - 100

for i in range(8):
    for j in range(i+1,9):
        if arr[i] + arr[j] == C:
            a = arr[i]
            b = arr[j]
            arr.remove(a)
            arr.remove(b)
            Break = False
            break
    if not Break:
        break 

    
for i in arr:
    print(i)            
        












