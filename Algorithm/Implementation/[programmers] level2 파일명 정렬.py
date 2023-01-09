def solution(files):

    def num_idx(str):

        flag = True

        for i in range(len(str)):
            if flag:
                if str[i].isdigit():
                    start_idx = i
                    flag = False
            else:

                if (i - start_idx) >=5:
                    end_idx = i
                    break

                if not str[i].isdigit():
                    end_idx = i
                    break
        else:
            end_idx = len(str)

        return start_idx, end_idx

    order = sorted(files, key = lambda x: (x[:num_idx(x)[0]].upper(),int(x[num_idx(x)[0]:num_idx(x)[1]]), files.index(x)))

    return order