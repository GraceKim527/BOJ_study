## 내 풀이

def solution(phone_number):
    num = len(phone_number)
    back = phone_number[-4:]
    return "*"*(num-4) + back

## 다른 사람의 풀이

def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]