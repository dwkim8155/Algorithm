N = int(input())
a, b = map(int, input().split())
c = int(input())

d_arr = []
for _ in range(N):
  d_arr.append(int(input()))

d_arr.sort(reverse=True)

total = c
ans = total/a
for i in range(len(d_arr)):
  price = a + b*(i+1)
  total += d_arr[i]
  tmp = (total/price)
  if ans < tmp:
    ans = tmp
  else:
    break
 
print(int(ans))