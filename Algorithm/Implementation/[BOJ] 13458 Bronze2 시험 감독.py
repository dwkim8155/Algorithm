num_room = int(input())
std_lst = list(map(int, input().split()))
ability = list(map(int, input().split()))

min_val = 0

for i in range(num_room):
    total_std = std_lst[i]

    total_std -= ability[0]
    min_val+=1
    if total_std <=0:
        continue

    min_val += ((total_std-1)//ability[1]) +1

print(min_val)