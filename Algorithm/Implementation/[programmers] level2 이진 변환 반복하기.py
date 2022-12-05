def solution(s):
    step = 0
    cnt = 0
    while s!="1":
        step+=1
        cnt +=s.count("0")
        m = s.replace("0","")
        s = bin(len(m))[2:]
  
    return [step,cnt]