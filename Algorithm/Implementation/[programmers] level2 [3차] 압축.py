def solution(msg):
    alpha_list = [chr(i) for i in range(65,91)]
    msg_list = list(reversed([msg[:i] for i in range(1,len(msg)+1)]))
    result = []

    while msg:

        msg_list = list(reversed([msg[:i] for i in range(1,len(msg)+1)]))

        for i in msg_list:
            if i in alpha_list:
                result.append(alpha_list.index(i)+1)
                msg = msg[len(i):]
                if msg:
                    alpha_list.append(i+msg[0])
                break


    return result