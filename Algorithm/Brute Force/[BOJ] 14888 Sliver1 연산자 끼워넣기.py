N = int(input())
num_arr = list(map(int, input().split()))
oper_arr = list(map(int, input().split()))

max_total = -float('inf')
min_total = float('inf')

def cal(start, oper_arr, num_arr):
    global max_total, min_total
    
    if not num_arr:
        if max_total < start:
            max_total = start
        
        if min_total > start:
            min_total = start
        return

    target = num_arr.pop(0)
    for idx, o in enumerate(["+", "-", "*", "/"]):
        if oper_arr[idx] !=0:
            result = operation(start, target ,o)
            oper_arr[idx]-=1
            cal(result, oper_arr[:], num_arr[:])
            oper_arr[idx]+=1
            

def operation(start, target, o):
    if o == "+":
        return start+target
    elif o == "-":
        return start-target
    elif o == "*":
        return start*target
    else:
        if start <0:
            return ((-start)//target)*-1
        else:
            return start//target    

start  = num_arr[0]
cal(start, oper_arr, num_arr[1:])
print(max_total)
print(min_total)