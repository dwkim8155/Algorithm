import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n,m = map(int, input().split())
p_arr = dict()
for i in range(n+1):
    p_arr[i]=i

def find(num):
    global p_arr
    if p_arr[num] == num:
        return num
    p_arr[num] = find(p_arr[num])
    return p_arr[num]

for _ in range(m):
    o,num1,num2 = map(int, input().split()) 
    p1 = find(num1)
    p2 = find(num2)
    if o==1:
        if p1==p2:
            print("YES")
        else:
            print("NO")
    else:
        if p1<=p2:
            p_arr[p2] = p1
        else:
            p_arr[p1] = p2
 
print()
