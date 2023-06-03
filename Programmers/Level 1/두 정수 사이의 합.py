## 내 풀이
def solution(a, b):
    sum = 0
    if a > b:
        for i in range(b, a+1):
            sum += i
    else:
        for i in range(a, b+1):
            sum += i
    return sum


## 다른 사람의 풀이

def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

print( adder(3, 5))