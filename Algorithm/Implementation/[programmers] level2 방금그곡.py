def solution(m, musicinfos):
    shap_list =["A#","C#","D#","F#","G#"]
    result_list = []
    idx_num = 2000

    def transition(str):
        nonlocal shap_list

        for shap in shap_list:
            str = str.replace(shap,shap[0].lower())
        return str

    new_m = transition(m)

    for i in musicinfos:
        info_list = i.split(",")
        start_len =  int(info_list[0][:2])*60 + int(info_list[0][3:5])
        end_len = int(info_list[1][:2])*60 + int(info_list[1][3:5])
        play_length = end_len - start_len
        melody = transition(info_list[3])
        play_melody = melody*(play_length//len(melody)) + melody[:(play_length%len(melody))]
        if new_m in play_melody:
            result_list.append((play_length, idx_num, info_list[2]))
            idx_num-=1

        result = sorted(result_list, reverse= True)
        if result:
            answer = result[0][2]
        else:
            answer="(None)"
            
    return answer

