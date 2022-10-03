import sys

input = sys.stdin.readline

while True:
    try:
        N = int(input())
    except:
        break
    val = 1
    while True:
        if val%N == 0:
            print(len(str(val)))
            break
        else:
            val = val*10 + 1

                
    