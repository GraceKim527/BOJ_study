## 내 풀이
def solution(seoul):
    index = seoul.index('Kim')
    answer = '김서방은 {}에 있다'.format(index)
    return answer

## 다른 사람의 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))