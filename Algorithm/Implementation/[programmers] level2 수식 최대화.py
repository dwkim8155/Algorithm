def solution(expression):

    answer = 0 
    pri = [['*','+','-'],['*','-','+'],['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+']]
    
    arr = []
    tmp = ''
    for ex in expression:
        if ex.isdigit():
            tmp+=ex
        else:
            arr.append(tmp)
            arr.append(ex)
            tmp=''
    arr.append(tmp)
    
    ex_arr = arr[:]
    
    for pr in pri:
        
        ex_arr = arr[:]    
        
        for op in pr:
            stack = []
            while len(ex_arr) != 0:
                tmp = ex_arr.pop(0)
                if tmp == op:
                    stack.append(str(eval(stack.pop()+tmp+ex_arr.pop(0))))
                        
                else:
                    stack.append(tmp)
            ex_arr = stack
           
        answer = max(abs(int(stack[0])),answer)
   
    return answer