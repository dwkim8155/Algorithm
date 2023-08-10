def solution(picks, minerals):

    min_tired = float('inf')

    def cal(picks, minerals, result):

        nonlocal min_tired

        if not minerals or sum(picks) ==0:
            if result< min_tired:
                min_tired=result
            return


        for i in range(3):
            if picks[i] !=0:
                total = 0
                for m in minerals[:5]:
                    if i==0:
                        total+=1
                    elif i==1:
                        if m=="diamond":
                            total +=5
                        else:
                            total+=1
                    else:
                        if m=="diamond":
                            total += 25
                        elif m=="iron":
                            total+=5
                        else:
                            total+=1

                picks[i]-=1
                result+=total
                cal(picks[:], minerals[5:], result)
                picks[i]+=1
                result-=total

    cal(picks, minerals, 0)

    return min_tired