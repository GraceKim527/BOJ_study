## 내 풀이
def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()
    return answer

## 다른 사람의 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]