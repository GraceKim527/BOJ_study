
def solution(s):
    s_s = s.split(' ')
    temp = []
    for i in s_s:
        i = i.capitalize()
        temp.append(i)
    return ' '.join(temp)

## 문법
# title() : 문장의 모든 단어의 첫 글자를 대문자로, 나머지는 소문자
# capitalize(): 문장의 첫 글자만 대문자로, 나머지는 소문자