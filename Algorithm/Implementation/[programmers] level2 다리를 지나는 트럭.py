def solution(bridge_length, weight, truck_weights):

    time = 0
    stack = []
    cnt = 0
    total = 0

    while True:
        if truck_weights and total+truck_weights[0] <=weight and cnt+1<=bridge_length:
            a = truck_weights.pop(0)
            stack.append(a)
            total += a
            cnt += 1
        else:
            break

    stack = stack + [0]*(bridge_length-len(stack))

    while total !=0:
        a = stack.pop(0)
        if a != 0:
            total -= a
            cnt -= 1

        if truck_weights and total+truck_weights[0] <=weight and cnt+1<=bridge_length:
            a = truck_weights.pop(0)
            stack.append(a)
            total += a
            cnt += 1
        else:
            stack.append(0)
        time+=1

    return time + bridge_length