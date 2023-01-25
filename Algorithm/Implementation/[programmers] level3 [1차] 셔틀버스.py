def solution(n, t, m, timetable):

    def minute(st):
        h = int(st[:2])
        return (h*60) + int(st[3:])

    def hhmm(time):
        s,r = divmod(time,60)
        h = str(s).rjust(2,"0")
        m = str(r).rjust(2,"0")    
        return h+':'+m

    time_arr = list(map(minute, timetable))   
    time_arr.sort()

    start = minute('09:00') - t
    stack = []

    for i in range(1,n+1):

        start += t 
        std = m
        for time in time_arr[:]:

            if std==0:
                break

            if time <=start:
                stack.append(time_arr.pop(0))
                std-=1


        if not time_arr or i==n:
            if std==0:
                return hhmm(stack[-1]-1)
            else:
                return hhmm(start)