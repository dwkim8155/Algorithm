def solution(s,e,num,st):

  if st == 1:
    print(' '*num, end="")
    return
  
  if (s==e):
      print('-', end="")  
      return
  else:
    itr = num//3
    for i in range(3):
      solution(s,s+itr-1,itr,i)
      s += itr 

while True:
  try:
    n = int(input())
    num = 3**n
    solution(1, num, num, 0)
    print()
  except:
    break