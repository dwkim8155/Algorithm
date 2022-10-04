N = int(input())

g_sum = 0

for i in range(1,N+1):
    g_sum += (N//i)*i

print(g_sum)
    