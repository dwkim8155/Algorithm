N = int(input())
ans = abs(N - 100)
Broken = int(input())


if Broken:
    Broken_arr = list(map(int, input().split()))
else:
    Broken_arr = []

for i in range(0,1000001):
    num = str(i)
    for j in num:
        if int(j) in Broken_arr:
            break
    else:
        ans = min(ans, len(num) + abs(N-i))
        
print(ans)
