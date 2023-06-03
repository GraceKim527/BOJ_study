## 내 풀이

def solution(a, b, n):
    answer = 0
    while True:
        if n < a: # 마트에 주어야하는 병 수보다 적게 남아있을 경우
            break
        take = n // a
        n = n - (a * take) + (take*b)
        answer += (take*b)
    return answer


## 다른 사람의 풀이
def solution(a, b, n):
    answer = 0
    while n >= a: # while문을 좀 더 효율적으로 써볼 것.
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer