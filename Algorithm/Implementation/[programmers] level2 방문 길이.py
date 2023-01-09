def solution(dirs):

    def move(str,cur):

        if str == "U":
            x,y = cur
            return  (x, y+1) if -5<= y+1 <=5 else (x,y)
        elif str == "D":
            x,y = cur
            return  (x, y-1) if -5<= y-1 <=5 else (x,y)
        elif str == "R":
            x,y = cur
            return  (x+1, y) if -5<= x+1 <=5 else (x,y)
        elif str == "L":
            x,y = cur
            return  (x-1, y) if -5<= x-1 <=5 else (x,y)

    arr = set()
    cur = (0,0)
    ans = 0

    for i in dirs:

        next_p = move(i,cur)

        if cur != next_p:
            if arr:
                for j in arr:
                    if len(set(j)&set((next_p,cur))) == 2:
                        break
                else:    
                    arr.add((next_p,cur))
            else:
                arr.add((next_p,cur))

        cur = next_p

    print(arr)

    return len(arr)