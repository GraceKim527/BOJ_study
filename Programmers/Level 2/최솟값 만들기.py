## 내 풀이

def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i] * B[i])
    return answer

## 다른 사람의 풀이

def getMinSum(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

## 하나는 오름차순, 하나는 내림차순 하는 것이 핵심이다.