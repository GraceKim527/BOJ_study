## 내 풀이

def solution(s):
    half = (len(s)+1) // 2
    if len(s) % 2 == 0 : return s[half-1:half+1]
    else : return s[half-1]

## 다른 사람의 풀이
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]