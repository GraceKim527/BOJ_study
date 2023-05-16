def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in s:
        if char in low:
            idx = low.find(char) + n
            answer += low[idx % 26]
        elif char in up:
            idx = up.find(char) + n
            answer += up[idx % 26]
        else:
            answer += " "
    return answer