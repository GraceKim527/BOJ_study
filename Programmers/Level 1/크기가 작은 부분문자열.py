def solution(t, p):
    answer = 0
    p_len = len(p) # 7
    t_len = len(t) # 3
    p = int(p)
    for i in range(t_len + 1 - p_len):
        if int(t[i:i+p_len]) <= p:
            answer += 1
    return answer